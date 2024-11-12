import subprocess
import time
from sqlalchemy.orm import Session
from src.DB.Connection import SessionLocal

from . import EventBusInstance
from src.Controller import InfoBaseController
from ..Enums import StateEnum

event_bus = EventBusInstance.event_bus

def launch_base(link_batch_files: [str]):
    db: Session = SessionLocal()

    # Liste des chemins vers les fichiers batch
    batch_files = link_batch_files

    # Dictionnaire pour stocker les processus
    processes = {}

    # Lancer tous les fichiers batch en parallèle
    for batch_file in batch_files:
        process = subprocess.Popen([batch_file])
        processes[batch_file] = process

    # Vérifier l'état de chaque processus
    while processes:
        for batch_file, process in list(processes.items()):
            if process.poll() is not None:  # Si le processus est terminé
                if process.returncode == 0:
                    print(f"{batch_file} a terminé avec succès.")
                    update_info_base = InfoBaseController.update_state_by_link_file_batch(
                        db=db,
                        link_file_batch=batch_file,
                        state=StateEnum.StateEnum.FINISHED
                    )
                    event_bus.emit("actualise_data", 1)
                else:
                    print(f"{batch_file} a échoué avec le code de retour : {process.returncode}")
                    update_info_base = InfoBaseController.update_state_by_link_file_batch(
                        db=db,
                        link_file_batch=batch_file,
                        state=StateEnum.StateEnum.ERROR
                    )
                    event_bus.emit("actualise_data", 1)

                # Supprimer le processus du dictionnaire une fois terminé
                processes.pop(batch_file)
            else:
                update_info_base = InfoBaseController.update_state_by_link_file_batch(
                    db=db,
                    link_file_batch=batch_file,
                    state=StateEnum.StateEnum.RUNNING
                )
                print(f"{batch_file} en cours.")
                event_bus.emit("actualise_data", 1)
        # Attendre un peu avant la prochaine vérification
        time.sleep(1)

    print("Tous les fichiers batch ont terminé.")
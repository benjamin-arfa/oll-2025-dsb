from src.model import Partei, Datenkatalog, Austauschvorgang, Storage, List


def who_are_parties(storage: Storage, parties: List[dict]) -> None:
    """Save all parties involved in the system"""
    for party in parties:
        storage.add(Partei.from_json(party))


def which_datasets_are_processed(storage: Storage, datasets: List[dict]) -> None:
    """Save all data catalogs being processed"""
    for dataset in datasets:
        storage.add(Datenkatalog.from_json(dataset))


def how_are_data_being_exchanged(storage: Storage, exchanges: List[dict]) -> None:
    """Save data exchange processes"""
    for exchange in exchanges:
        storage.add(Austauschvorgang.from_json(exchange))

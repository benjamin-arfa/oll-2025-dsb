def who_are_parties(storage: Storage, parties: List[Partei]) -> None:
    """Save all parties involved in the system"""
    for party in parties:
        storage.save(party)

def which_datasets_are_processed(storage: Storage, datasets: List[Datenkatalog]) -> None:
    """Save all data catalogs being processed"""
    for dataset in datasets:
        storage.save(dataset)

def how_are_data_being_exchanged(storage: Storage, exchanges: List[Austauschvorgang]) -> None:
    """Save data exchange processes"""
    for exchange in exchanges:
        storage.save(exchange)

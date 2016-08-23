
class PipelineReport:
    """Records executed pipeline filters and actions"""

    def __init__(self):
        self.records = []

    def add_record(self, name, description, elapsed):
        self.records.append({
            'name': name,
            'description': description,
            'elapsed': elapsed
        })

    def get_totaltime(self):
        return sum([record['elapsed'] for record in self.records])

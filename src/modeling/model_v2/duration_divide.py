class DurationPlaceDivider:
    def __init__(self, data):
        self.data = data
        self.slices = [data[i:i + 3][['id', 'place_name']].reset_index(drop=True) for i in range(0, len(data), 3)]

    def divide_durations_place_name(self, max_days=None):
        if max_days is None:
            max_days = len(self.slices)

        sliced_data = []
        for i, slices in enumerate(self.slices[:max_days], start=1):
            day_slices = []
            for _, row in slices.iterrows():
                day_slices.append({'id': row['id'], 'place_name': row['place_name']})
            sliced_data.append(day_slices)

        return sliced_data


import pandas as pd

class NJCleaner:
    def __init__(self, csv_path):
        self.data = pd.read_csv(csv_path)

    def order_by_scheduled_time(self) -> pd.DataFrame:
        sorted_df = self.data.sort_values('scheduled_time')
        return sorted_df

    def drop_columns_and_nan(self) -> pd.DataFrame:
        self.data = self.data.drop(['from', 'to'], axis=1)
        self.data = self.data.dropna()
        return self.data

    def convert_date_to_day(self) -> pd.DataFrame:
        self.data['day'] = pd.to_datetime(self.data['date']).dt.day_name()
        self.data = self.data.drop('date', axis=1)
        return self.data

    def convert_scheduled_time_to_part_of_the_day(self) -> pd.DataFrame:
        """4:00-7:59 -- early_morning
         8:00-11:59 -- morning
         12:00-15:59 -- afternoon
         16:00-19:59 -- evening
         20:00-23:59 -- night
         0:00-3:59 -- late_night """

        def part_of_the_day(hour):
            if 4 <= hour < 8:
                return 'early_morning'
            elif 8 <= hour < 12:
                return 'morning'
            elif 12 <= hour < 16:
                return 'afternoon'
            elif 16 <= hour < 20:
                return 'evening'
            elif hour >= 20 or hour < 4:
                return 'night'

        self.data['part_of_the_day'] = self.data['scheduled_time'].apply(lambda x: part_of_the_day(x.hour))
        self.data = self.data.drop('scheduled_time', axis=1)
        return self.data

    def convert_delay(self) -> pd.DataFrame:
        def calculate_delay(minutes):
            if 0 <= minutes <  5:
                return 0
            elif 5 <= minutes:
                return 1

        self.data['delay'] = self.data['delay_minutes'].apply(lambda x: calculate_delay(x))
        return self.data

    def drop_unnecessary_columns(self) -> pd.DataFrame:
        self.data = self.data.drop(['train_id', 'scheduled_time', 'actual_time', 'delay_minutes'], axis=1)
        return self.data

    def save_first_60k(self, csv_save_path: str) -> pd.DataFrame:
        self.data[:60000].to_csv(csv_save_path, index=False)
        return self.data

    def prep_df(self, csv_save_path: str = 'data/NJ.csv'):
        self.order_by_scheduled_time()
        self.drop_columns_and_nan()
        self.convert_date_to_day()
        self.convert_scheduled_time_to_part_of_the_day()
        self.convert_delay()
        self.drop_unnecessary_columns()
        self.save_first_60k(csv_save_path)
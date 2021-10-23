import os
from typing import List
import csv

import pandas as pd


class SqFrame:
    DATA_INPUT_DIR = "data-input"

    def __init__(self, csv_src_name: str) -> None:
        src_file_path = os.path.join(self.DATA_INPUT_DIR, csv_src_name)
        self.sq_df = pd.read_csv(src_file_path)

        self.aggregate_months = self._aggregate_months()
        self.aggregate_exercise_types = self._aggregate_exercise_types()

    def write_data_to_disk(self):
        self._write_month_data_to_file()
        self._write_exercise_type_data_to_file()

    def _aggregate_months(self) -> dict:
        month_keys = {
            "01": "January",
            "02": "February",
            "03": "March",
            "04": "April",
            "05": "May",
            "06": "June",
            "07": "July",
            "08": "August",
            "09": "September",
            "10": "October",
            "11": "November",
            "12": "December"
        }
        month_count = {
            "January": 0,
            "February": 0,
            "March": 0,
            "April": 0,
            "May": 0,
            "June": 0,
            "July": 0,
            "August": 0,
            "September": 0,
            "October": 0,
            "November": 0,
            "December": 0
        }

        for index, row in self.sq_df.iterrows():
            date_str = row["Date"].split("/")[0]
            month_key = month_keys[date_str]
            current_count = month_count[month_key]
            current_count += 1
            month_count[month_key] = current_count
        
        return month_count

    def _aggregate_exercise_types(self) -> dict:
        exercise_types = self._get_unique_descriptions()
        
        for exercise in exercise_types:
            filtered_frame = self.sq_df[self.sq_df["Data"] == exercise]
            count = filtered_frame.shape[0]
            exercise_types[exercise] = count

        return exercise_types

    def _get_unique_descriptions(self) -> dict:
        descriptions = self.sq_df["Data"].to_numpy()
        # Hash map is fast for lookup
        unique_descriptions = {}
        for description in descriptions:
            if unique_descriptions.get(description) is None:
                unique_descriptions[description] = 0
        
        return unique_descriptions

    def _write_month_data_to_file(self):
        output_file_path = os.path.join("data-output","exercise_month_aggregates.csv")
        with open(output_file_path, "w") as sink_file:
            csv_writer = csv.writer(sink_file)
            csv_writer.writerow(["Month", "Exercise count"])
            for month, count in self.aggregate_months.items():
                csv_writer.writerow([month, count])
        
    def _write_exercise_type_data_to_file(self):
        output_file_path = os.path.join("data-output","exercise_type_aggregates.csv")
        with open(output_file_path, "w") as sink_file:
            csv_writer = csv.writer(sink_file)
            csv_writer.writerow(["Exercise type", "Count"])
            for exercise_type, count in self.aggregate_exercise_types.items():
                csv_writer.writerow([exercise_type, count])


if __name__ == "__main__":
    src_file = "sq_manual_2021.csv"
    sq_frame = SqFrame(src_file)
    sq_frame.write_data_to_disk()
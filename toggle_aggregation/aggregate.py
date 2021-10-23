from toggle_aggregation.models.toggle_df import ToggleFrame


def print_toggle_data():
    toggle_file_name = "toggl_2021.csv"
    toggle_frame = ToggleFrame(toggle_file_name)
    # toggle_frame.print_aggregated_descriptions()
    toggle_frame.write_month_aggregates_to_file()

if __name__  == "__main__":
    print_toggle_data()
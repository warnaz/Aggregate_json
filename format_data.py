import pandas as pd
import json


def aggregate_salary_data(dt_from, dt_upto, group_type):
    labels = []
    data_path = "output_json_file.json"
    data = pd.read_json(data_path)
    data["dt"] = pd.to_datetime(data["dt"])
    filtered_data = data[(data["dt"] >= dt_from) & (data["dt"] <= dt_upto)]

    if group_type == "hour":
        dt_from = pd.to_datetime(dt_from)
        dt_upto = pd.to_datetime(dt_upto)

        all_hours = pd.date_range(start=dt_from, end=dt_upto, freq='H')

        filtered_data['hour'] = filtered_data['dt'].dt.hour

        grouped_data = filtered_data.groupby(
            [filtered_data['dt'].dt.floor('h')])['value'].sum()

        grouped_data = grouped_data.reindex(all_hours, fill_value=0)

    elif group_type == "day":
        dt_from = pd.to_datetime(dt_from)
        dt_upto = pd.to_datetime(dt_upto)

        all_dates = pd.date_range(start=dt_from, end=dt_upto, freq='D')

        grouped_data = filtered_data.groupby(
            filtered_data["dt"].dt.date)["value"].sum()

        grouped_data = grouped_data.reindex(all_dates, fill_value=0)

    elif group_type == "month":
        grouped_data = filtered_data.groupby(
            pd.Grouper(key="dt", freq="MS"))["value"].sum()
    else:
        raise ValueError(f"Unknown aggregation type: {group_type}")

    if isinstance(grouped_data.index, pd.PeriodIndex):
        labels = grouped_data.index.to_timestamp().isoformat().tolist()
    elif isinstance(grouped_data.index, pd.DatetimeIndex):
        labels = grouped_data.index.strftime('%Y-%m-%dT%H:%M:%S').tolist()
    else:
        labels = grouped_data.index.astype(str).tolist()

    dataset = grouped_data.values.tolist()
    result = {"dataset": dataset, "labels": labels}
    return json.dumps(result)

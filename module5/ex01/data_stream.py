from abc import ABC, abstractmethod
import sys
from optparse import Option
from typing import Any, List, Optional, Dict, Union



class DataStream(ABC):
    def __init__(self, stream_id:str):
        self.stream_id = stream_id
    @abstractmethod
    def process_batch(self, data_bach: List[Any]) -> str:
        pass

    def filter_data(self,data_bach: List[Any], criteria: Optional[str] = None) -> List[Any]:
        if criteria is None:
            return data_bach
        return [item for item in data_bach if criteria in str(item)]

    def get_stats(self) -> Dict[str, Union[str,int,float]]:
        return {"id": self.stream_id, "status": "active"}

class SensorStream(DataStream):
    def __init__(self, stream_id:str):
        super().__init__(stream_id)
        self.type = "Environmental data"
        self.count = 0
        self.avg_temp = 0
    def process_batch(self, data_bach: List[Any]) -> str:
        self.count = len(data_bach)
        temps = [d["temp"] for d in data_bach if isinstance(d,dict) and "temp" in d]
        if temps:
            self.avg_temp = sum(temps)/len(temps)
        return f"Stream ID: {self.stream_id}, Type: {self.type}\nProcessing sensor batch: {data_bach}"

    def filter_data(self,data_bach: List[Any], criteria: Optional[str] = None) -> List[Any]:
        if not criteria:
            return data_bach
        return[
            item for item in data_bach
            if isinstance(item,dict) and any(criteria is str(k) or criteria in str(v) for k,v in item.items())
        ]
    def get_stats(self) -> Dict[str, Union[str,int,float]]:
        return{
            self.count: "readings processed",
            "avg_temp": self.avg_temp,
        }

class TransactionStream(DataStream):
    def __init__(self, stream_id:str):
        super().__init__(stream_id)
        self.type = "Transaction data"
        self.operations = 0
        self.net_flow = 0
    def process_batch(self, data_bach: List[Any]) -> str:
        self.operations += len(data_bach)
        for item in data_bach:
            if ":" in str(item):
                action, amount = str(item).split(":")
                val = int(amount)
                if action.lower() == "buy":
                    self.net_flow += val
                elif action.lower() == "sell":
                    self.net_flow -= val
        return f"Stream ID: {self.stream_id}, Type: {self.type}\nProcessing transaction: {data_bach}"
    def filter_data(self,data_bach: List[Any], criteria: Optional[str] = None) -> List[Any]:
        if not criteria:
            return data_bach
        return[
            item for item in data_bach
            if criteria.lower() in str(item).lower()
        ]
    def get_stats(self) -> Dict[str, Union[str,int,float]]:
        return {
            "operations": self.operations,
            "net_flow": f"{'+' if self.net_flow >= 0 else '-'}{self.net_flow}units"
        }

class EventStream(DataStream):
    def __init__(self, stream_id:str):
        super().__init__(stream_id)
        self.type = "Event data"
        self.count = 0
        self.errors = 0
    def process_batch(self, data_bach: List[Any]) -> str:
        self.count = len(data_bach)
        for item in data_bach:
            if item.lower() == "error":
                self.errors += 1
        return f"Stream ID: {self.stream_id}, Type: {self.type}\nProcessing event: {data_bach}"

    def filter_data(self,data_bach: List[Any], criteria: Optional[str] = None) -> List[Any]:
        if not criteria:
            return data_bach
        return[
            item for item in data_bach if str(item).lower() == criteria.lower()
        ]
    def get_stats(self) -> Dict[str, Union[str,int,float]]:
        return{
            "events" : self.count,
            "error detected" : self.errors,
        }

class StreamProcessor:
    def __init__(self):
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream):
        self.streams.append(stream)

    def process_all(self, batches: List[List[Any]]):
        print("=== Polymorphic Stream Processing ===")
        print("Processing mixed stream types through unified interface...")
        for stream, batch in zip(self.streams, batches):
            try:
                result = stream.process_batch(batch)
                print(result)
                print(f"Analysis: {stream.get_stats()}")
            except Exception as e:
                print(f"Error processing stream {stream.stream_id}: {e}")
        pass

if __name__ == "__main__":
    processor = StreamProcessor()
    sensor = SensorStream("Sensor 1")
    transaction = TransactionStream("Transaction 1")
    event = EventStream("Event 1")

    processor.add_stream(sensor)
    processor.add_stream(transaction)
    processor.add_stream(event)

    print(f"Code Nexus")
    sensor_data = [{"temp": 22.5}, {"humidity": 65}, {"pressure": 1013}]
    transaction_data = ["buy:100", "sell:150", "buy:75"]
    event_data = ["login", "error", "logout"]
    all_batches = [sensor_data, transaction_data, event_data]
    processor.process_all(all_batches)


    print(f"Filtering active")
    critical_events = event.filter_data(event_data, criteria="error")
    large_trans = transaction.filter_data(transaction_data, criteria="buy")
    print(f"Filtered results: {len(critical_events)} critical sensor alerts, {len(large_trans)} large transaction(s)")
    print("All streams processed successfully. Nexus throughput optimal.")


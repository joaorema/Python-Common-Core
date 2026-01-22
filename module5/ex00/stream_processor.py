from abc import ABC, abstractmethod
from operator import truediv
from pickle import LIST
from typing import Any

#Data Processor abstract class using ABC and abstract method
class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass
    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass
    def format_output(self, data: str) -> str:
        return f"Output : "

class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        return isinstance(data, list) and all(isinstance(x, (int, float)) for x in data)
    def process(self, data: Any) -> str:
        print(f"Initializing Numeric Processor...")
        print(f"Processing Data: {data}")
        if not self.validate(data):
            return "Invalid data for numeric processing"
        print(f"Validation: Numeric data verified")
        total = sum(data)
        avg = total / len(data) if data else 0
        result = f"Processed {len(data)} numeric values, sum={total}, avg={avg}"
        return self.format_output(result)
    def format_output(self, data: str) -> str:
        base = super().format_output(data)
        return f"{base}{data}"


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data,str):
            return True
        else:
            return False
    def process(self, data: Any) -> str:
        print(f"Initializing Text Processor...")
        print(f"Processing Data: {data}")
        if not self.validate(data):
            return "Invalid data for text processing"
        print(f"Validation: Text data verified")
        result = f"Processed text: {len(data)} characters, {len(data.split())} words"
        return self.format_output(result)

    def format_output(self, data: str) -> str:
        base = super().format_output(data)
        return f"{base} {data}"

class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        print(f"Initializing Log Processor...")
        print(f"Processing Data: {data}")
        if not isinstance(data, str):
            return False
        print(f"Validation: Log entry verified")
        return any(level in data for level in ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"))
    def process(self, data: Any) -> str:
        if not self.validate(data):
            return "Invalid data for log processing"

        result = f"Log Processor: {data}"
        return self.format_output(result)
    def format_output(self, data: str) -> str:
        base_format = super().format_output(data)
        return f"{base_format}[ALERT] ERROR level detected: connection timeout"

def stream_processor():
    print(f"=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")
    print()
    n_proc = NumericProcessor()
    num_data = [1, 2, 3, 4, 5]
    if n_proc.validate(num_data):
        print(n_proc.process(num_data))
    print()

    t_proc = TextProcessor()
    text_data = "Hello Nexus World"
    if t_proc.validate(text_data):
        print(t_proc.process(text_data))
    print()

    processors =[NumericProcessor(), TextProcessor(), LogProcessor()]
    data_items = [[1,2,3], "Hello world!", "INFO No errors"]
    for i, proc in enumerate(processors):
        result = proc.process(data_items[i])
        print(f"Result: {i+1}: {result.replace('Output: ', '')}")




if __name__ == "__main__":
    stream_processor()

    pass
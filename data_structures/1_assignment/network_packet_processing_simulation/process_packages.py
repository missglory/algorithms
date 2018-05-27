# python3
import sys, os

class Request:
    def __init__(self, arrival_time, process_time):
        self.arrival_time = arrival_time
        self.process_time = process_time

class Response:
    def __init__(self, dropped, start_time):
        self.dropped = dropped
        self.start_time = start_time

class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time_ = []

    def Process(self, request):
        # write your code here
        while len(self.finish_time_) and self.finish_time_[0] <= request.arrival_time:
            self.finish_time_.pop(0)
        if not len(self.finish_time_):
            self.finish_time_.append(request.arrival_time + request.process_time)
            return Response(False, request.arrival_time)
        tail = self.finish_time_[len(self.finish_time_)-1]
        if len(self.finish_time_) < self.size:
            self.finish_time_.append(tail + request.process_time)
            return Response(False, tail)
        else:
            return Response(True, -1)

def ReadRequests(count):
    requests = []
    for i in range(count):
        arrival_time, process_time = map(int, input().strip().split())
        requests.append(Request(arrival_time, process_time))
    return requests

def ProcessRequests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.Process(request))
    return responses

def PrintResponses(responses):
    for response in responses:
        print(response.start_time if not response.dropped else -1)

if __name__ == "__main__":
    # sys.stdin = open(f'{os.path.abspath(__file__)}\\..\\tests\\06')
    size, count = map(int, input().strip().split())
    requests = ReadRequests(count)

    buffer = Buffer(size)
    responses = ProcessRequests(requests, buffer)

    PrintResponses(responses)

import heapq

def parallel_processing(n, m, data):
    start_time = [0] * n
    output = []
    heap = [(0, i) for i in range(n)]

    for i in range(m):
        processing_time = data[i]
        end_time, thread_idx = heapq.heappop(heap)
        output.append((thread_idx, start_time[thread_idx]))
        start_time[thread_idx] = end_time + processing_time
        heapq.heappush(heap, (start_time[thread_idx], thread_idx))

    return output

def main():
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    output = parallel_processing(n, m, data)
    for thread_idx, start_time in output:
        print(thread_idx, start_time)
if __name__ == "__main__":
    main()

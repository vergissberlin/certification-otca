# Solution: Signals - Metrics

## Solution Overview

This solution covers creating and using different metric types with labels.

## Step-by-Step Solution

### Task 1: Create Different Metric Types

**Counter** (already exists):
```javascript
const requestCounter = meter.createCounter('requests_total');
requestCounter.add(1);
```

**Gauge**:
```javascript
const memoryGauge = meter.createObservableGauge('memory_usage_bytes');
memoryGauge.addCallback((observableResult) => {
  observableResult.observe(process.memoryUsage().heapUsed);
});
```

**Histogram**:
```javascript
const responseTimeHistogram = meter.createHistogram('http_request_duration_seconds');
const start = Date.now();
// ... operation ...
responseTimeHistogram.record((Date.now() - start) / 1000);
```

### Task 2: Add Metric Labels

Modify counter to include labels:

```javascript
const requestCounter = meter.createCounter('requests_total', {
  description: 'Total number of requests'
});

app.get('/hello', (req, res) => {
  requestCounter.add(1, {
    'method': 'GET',
    'route': '/hello',
    'status': '200'
  });
  res.send('Hello from Node Service!');
});
```

**Prometheus Query**: `requests_total{method="GET", route="/hello"}`

### Task 3: Record Metric Values

**Counter**: `counter.add(value, labels)`
**Gauge**: `gauge.record(value, labels)` or observable callback
**Histogram**: `histogram.record(value, labels)`

### Task 4: Understand Aggregation

**Prometheus Queries**:
- `requests_total` - Total count
- `rate(requests_total[1m])` - Requests per second
- `sum(rate(requests_total[1m]))` - Total rate
- `sum(rate(requests_total[1m])) by (method)` - Rate by method

## Key Takeaways

- Counter: Cumulative values
- Gauge: Current values
- Histogram: Distributions
- Labels add dimensionality
- Aggregation happens in backends

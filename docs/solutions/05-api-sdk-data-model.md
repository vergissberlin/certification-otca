# Solution: Data Model

## Solution Overview

This solution covers understanding and working with OpenTelemetry data model components.

## Step-by-Step Solution

### Task 4: Create Different Metric Types

**Add Gauge Metric** (in `service-node/app.js`):

```javascript
const memoryGauge = meter.createObservableGauge('memory_usage_bytes', {
  description: 'Current memory usage in bytes'
});

memoryGauge.addCallback((observableResult) => {
  const memoryUsage = process.memoryUsage().heapUsed;
  observableResult.observe(memoryUsage);
});
```

**Add Histogram Metric** (in `service-node/app.js`):

```javascript
const responseTimeHistogram = meter.createHistogram('http_request_duration_seconds', {
  description: 'HTTP request duration in seconds'
});

app.get('/hello', (req, res) => {
  const start = Date.now();
  requestCounter.add(1);
  res.send('Hello from Node Service!');
  const duration = (Date.now() - start) / 1000;
  responseTimeHistogram.record(duration);
});
```

**Verification**:
- Check Prometheus for new metrics
- Gauge: `memory_usage_bytes`
- Histogram: `http_request_duration_seconds`
- Query histogram: `histogram_quantile(0.95, http_request_duration_seconds_bucket)`

## Key Takeaways

- **Counter**: Cumulative, increasing values (requests_total)
- **Gauge**: Current value, can go up/down (memory usage)
- **Histogram**: Distribution of values (response times)
- Choose metric type based on what you're measuring

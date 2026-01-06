# Solution: Signals - Logs

## Solution Overview

This solution covers integrating OpenTelemetry logging (note: logs signal is newer and may require additional setup).

## Step-by-Step Solution

### Task 2: Add Logging Instrumentation

**Note**: OpenTelemetry logging is still evolving. For now, we can correlate logs with traces.

**Option 1: Add Trace Context to Logs** (in `service-node/app.js`):

```javascript
const { trace } = require('@opentelemetry/api');

app.get('/hello', (req, res) => {
  const span = trace.getActiveSpan();
  const traceId = span?.spanContext().traceId;
  const spanId = span?.spanContext().spanId;
  
  console.log(JSON.stringify({
    message: 'Processing request',
    traceId: traceId,
    spanId: spanId,
    timestamp: new Date().toISOString()
  }));
  
  requestCounter.add(1);
  res.send('Hello from Node Service!');
});
```

### Task 3: Correlate Logs with Traces

The trace ID and span ID in logs allow correlation with traces in Jaeger.

**Verification**:
1. Make request and check console logs
2. Note trace ID from logs
3. Search for trace ID in Jaeger
4. Correlate log with trace

## Key Takeaways

- Logs signal is newer in OpenTelemetry
- Correlate logs with traces using trace ID
- Include trace context in log messages
- Full logging SDK support coming

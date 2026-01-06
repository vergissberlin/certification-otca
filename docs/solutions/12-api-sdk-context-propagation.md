# Solution: Context Propagation

## Solution Overview

This solution covers understanding and verifying context propagation in distributed tracing.

## Step-by-Step Solution

### Task 2: Verify Automatic Propagation

Modify `service-node/app.js` to call Python service:

```javascript
const axios = require('axios');

app.get('/hello', async (req, res) => {
  // Context automatically propagated via HTTP headers
  const response = await axios.get('http://service-python:5000/hello');
  requestCounter.add(1);
  res.send(`Node + Python: ${response.data}`);
});
```

**Verification**:
1. Make request to Node service
2. Check Jaeger → Should see trace spanning both services
3. Verify trace ID is same across services

### Task 3: Inspect Trace Context

**Trace Context Header** (`traceparent`):
```
traceparent: 00-4bf92f3577b34da6a3ce929d0e0e4736-00f067aa0ba902b7-01
```

**Format**: `version-trace_id-parent_id-trace_flags`

**Components**:
- `version`: 00 (current version)
- `trace_id`: 128-bit trace identifier
- `parent_id`: 64-bit parent span identifier
- `trace_flags`: Flags (01 = sampled)

**Inspect in Code**:
```javascript
const { trace } = require('@opentelemetry/api');
const span = trace.getActiveSpan();
const context = span?.spanContext();
console.log('Trace ID:', context.traceId);
console.log('Span ID:', context.spanId);
```

## Key Takeaways

- Context propagation is automatic with instrumentation
- W3C Trace Context standard format
- Propagated via HTTP headers
- Enables distributed tracing

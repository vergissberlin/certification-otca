# Solution: Debugging Context Propagation

## Solution Overview

This solution covers debugging context propagation issues.

## Step-by-Step Solution

### Task 1: Identify Issues

**Symptoms of Broken Propagation**:
- Separate traces instead of one distributed trace
- Missing trace IDs in logs
- Orphaned spans in Jaeger
- No parent-child relationships

**Check Jaeger**: Look for traces that should be connected but aren't.

### Task 2: Inspect Trace Context

**Inspect HTTP Headers**:
```bash
curl -v http://localhost:3000/hello
```

Look for `traceparent` header in response.

**In Code**:
```javascript
app.get('/hello', (req, res) => {
  console.log('Traceparent header:', req.headers.traceparent);
  const span = trace.getActiveSpan();
  console.log('Active span context:', span?.spanContext());
});
```

### Task 3: Debug Propagation Problems

**Common Issues**:
1. Missing instrumentation
2. Proxy stripping headers
3. Incorrect propagator configuration
4. Network issues

**Fix**: Ensure instrumentation is properly configured and headers aren't stripped.

### Task 4: Verify Propagation

**Test Cross-Service**:
1. Make request from Node to Python
2. Check Jaeger for correlated trace
3. Verify same trace ID across services
4. Check parent-child relationships

## Key Takeaways

- Check for `traceparent` header
- Verify instrumentation is active
- Check for proxy/network issues
- Verify in Jaeger UI

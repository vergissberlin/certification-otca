# Solution: Instrumentation

## Solution Overview

This solution covers adding manual instrumentation and understanding the combination of automatic and manual instrumentation.

## Step-by-Step Solution

### Task 2: Add Manual Instrumentation

In `service-node/app.js`, add manual span:

```javascript
const { trace } = require('@opentelemetry/api');
const tracer = trace.getTracer('service-node-manual');

app.get('/hello', (req, res) => {
  const span = tracer.startSpan('manual-operation');
  span.setAttribute('operation.type', 'hello');
  
  try {
    requestCounter.add(1);
    span.addEvent('Counter incremented');
    res.send('Hello from Node Service!');
    span.setStatus({ code: trace.SpanStatusCode.OK });
  } catch (error) {
    span.setStatus({ 
      code: trace.SpanStatusCode.ERROR, 
      message: error.message 
    });
    throw error;
  } finally {
    span.end();
  }
});
```

**Verification**: Check Jaeger UI → See manual span within automatic Express span.

### Task 3: Configure Automatic Instrumentation

Modify Express instrumentation in `service-node/app.js`:

```javascript
registerInstrumentations({
  instrumentations: [
    new ExpressInstrumentation({
      ignoreIncomingRequestHook: (req) => {
        // Ignore health check endpoints
        return req.url === '/health';
      }
    })
  ],
});
```

### Task 4: Combine Automatic and Manual

The manual span from Task 2 will automatically be a child of the automatic Express span due to context propagation.

**Verification**:

- Check Jaeger UI
- See span hierarchy: Express span (automatic) → manual-operation span (manual)
- Verify parent-child relationship

## Key Takeaways

- Automatic instrumentation: Easy setup, covers common cases
- Manual instrumentation: Full control, business logic tracking
- Combine both for complete observability
- Context propagation maintains span relationships

# Solution: Signals - Tracing

## Solution Overview

This solution covers creating and managing spans for distributed tracing.

## Step-by-Step Solution

### Task 1: Create Manual Spans

In `service-node/app.js`:

```javascript
const { trace } = require('@opentelemetry/api');
const tracer = trace.getTracer('service-node');

app.get('/hello', (req, res) => {
  const span = tracer.startSpan('hello-operation');
  span.setAttribute('operation.type', 'greeting');
  span.setAttribute('user.agent', req.headers['user-agent']);
  
  try {
    requestCounter.add(1);
    res.send('Hello from Node Service!');
    span.setStatus({ code: trace.SpanStatusCode.OK });
  } catch (error) {
    span.setStatus({ 
      code: trace.SpanStatusCode.ERROR,
      message: error.message 
    });
    span.recordException(error);
    throw error;
  } finally {
    span.end();
  }
});
```

### Task 2: Add Span Attributes and Events

```javascript
span.setAttribute('http.method', 'GET');
span.setAttribute('http.route', '/hello');
span.addEvent('Request received', {
  'timestamp': Date.now()
});
span.addEvent('Response sent', {
  'status': 200
});
```

### Task 3: Set Span Status

```javascript
// Success
span.setStatus({ code: trace.SpanStatusCode.OK });

// Error
span.setStatus({ 
  code: trace.SpanStatusCode.ERROR,
  message: 'Operation failed' 
});
span.recordException(error);
```

### Task 4: Create Distributed Traces

Modify `service-node/app.js` to call Python service:

```javascript
const axios = require('axios');

app.get('/hello', async (req, res) => {
  const span = tracer.startSpan('node-hello-operation');
  
  try {
    // Call Python service - context automatically propagated
    const response = await axios.get('http://service-python:5000/hello');
    requestCounter.add(1);
    res.send(`Hello from Node Service! Python says: ${response.data}`);
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

**Verification**: Check Jaeger → See trace spanning both services.

## Key Takeaways

- Spans represent operations
- Attributes provide context
- Events mark important moments
- Status indicates success/failure
- Context propagation enables distributed tracing

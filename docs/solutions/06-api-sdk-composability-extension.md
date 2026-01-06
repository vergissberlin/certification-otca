# Solution: Composability and Extension

## Solution Overview

This solution covers understanding and extending OpenTelemetry's composable architecture.

## Step-by-Step Solution

### Task 2: Modify Span Processors

Modify `service-node/app.js` to configure BatchSpanProcessor:

```javascript
const { BatchSpanProcessor } = require('@opentelemetry/sdk-trace-base');

tracerProvider.addSpanProcessor(
  new BatchSpanProcessor(new OTLPTraceExporter(), {
    maxQueueSize: 2048,
    maxExportBatchSize: 512,
    exportTimeoutMillis: 30000,
    scheduledDelayMillis: 5000
  })
);
```

**Configuration Options**:
- `maxQueueSize`: Maximum queue size
- `maxExportBatchSize`: Batch size for export
- `exportTimeoutMillis`: Export timeout
- `scheduledDelayMillis`: Delay between exports

### Task 4: Add Custom Span Processor

Create a simple custom processor in `service-node/app.js`:

```javascript
const { SpanProcessor } = require('@opentelemetry/sdk-trace-base');

class CustomSpanProcessor extends SpanProcessor {
  onStart(span) {
    // Add custom attribute to all spans
    span.setAttribute('custom.processor', 'enabled');
  }

  onEnd(span) {
    // Process span before export
    console.log(`Span ended: ${span.name}`);
  }

  shutdown() {
    return Promise.resolve();
  }

  forceFlush() {
    return Promise.resolve();
  }
}

// Add custom processor
tracerProvider.addSpanProcessor(new CustomSpanProcessor());
tracerProvider.addSpanProcessor(new BatchSpanProcessor(new OTLPTraceExporter()));
```

**Verification**: Check Jaeger → All spans should have `custom.processor: enabled` attribute.

## Key Takeaways

- OpenTelemetry is highly composable
- Processors can modify data before export
- Custom processors for business logic
- Multiple processors can be chained

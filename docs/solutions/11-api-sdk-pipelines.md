# Solution: SDK Pipelines

## Solution Overview

This solution covers understanding and configuring SDK pipelines for traces and metrics.

## Step-by-Step Solution

### Task 1: Identify Trace Pipeline

**Current Trace Pipeline** (in `service-node/app.js`):
```
TracerProvider → BatchSpanProcessor → OTLPTraceExporter → Collector
```

**Components**:
- `TracerProvider`: Creates and manages tracers
- `BatchSpanProcessor`: Batches spans before export
- `OTLPTraceExporter`: Exports spans via OTLP

### Task 2: Identify Metrics Pipeline

**Current Metrics Pipeline** (in `service-node/app.js`):
```
MeterProvider → PeriodicExportingMetricReader → OTLPMetricExporter → Collector
```

**Components**:
- `MeterProvider`: Creates and manages meters
- `PeriodicExportingMetricReader`: Periodically exports metrics
- `OTLPMetricExporter`: Exports metrics via OTLP

### Task 3: Modify Pipeline Configuration

Modify `service-node/app.js`:

```javascript
// Configure batch processor
tracerProvider.addSpanProcessor(
  new BatchSpanProcessor(new OTLPTraceExporter(), {
    maxQueueSize: 2048,
    maxExportBatchSize: 512,
    exportTimeoutMillis: 30000,
    scheduledDelayMillis: 5000
  })
);

// Configure metric reader
const meterProvider = new MeterProvider({
  metricReaders: [
    new PeriodicExportingMetricReader({
      exporter: new OTLPMetricExporter(),
      exportIntervalMillis: 10000 // Export every 10 seconds
    })
  ]
});
```

## Key Takeaways

- Trace pipeline: TracerProvider → Processor → Exporter
- Metrics pipeline: MeterProvider → Reader → Exporter
- Pipelines are configurable
- Components process data before export

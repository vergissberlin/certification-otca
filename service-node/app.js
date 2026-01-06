const express = require('express');
const { NodeTracerProvider } = require('@opentelemetry/sdk-trace-node');
const { registerInstrumentations } = require('@opentelemetry/instrumentation');
const { ExpressInstrumentation } = require('@opentelemetry/instrumentation-express');
const { OTLPTraceExporter } = require('@opentelemetry/exporter-trace-otlp-grpc');
const { BatchSpanProcessor } = require('@opentelemetry/sdk-trace-base');
const { MeterProvider, PeriodicExportingMetricReader } = require('@opentelemetry/sdk-metrics');
const { OTLPMetricExporter } = require('@opentelemetry/exporter-metrics-otlp-proto');

const app = express();

const tracerProvider = new NodeTracerProvider();
tracerProvider.addSpanProcessor(new BatchSpanProcessor(new OTLPTraceExporter()));
tracerProvider.register();

const meterProvider = new MeterProvider({
  metricReaders: [new PeriodicExportingMetricReader({ exporter: new OTLPMetricExporter() })]
});
const meter = meterProvider.getMeter('service-node-meter');
const requestCounter = meter.createCounter('requests_total');

registerInstrumentations({
  instrumentations: [new ExpressInstrumentation()],
});

app.get('/hello', (req, res) => {
  requestCounter.add(1);
  res.send('Hello from Node Service!');
});

app.listen(3000, () => console.log('Node Service listening on port 3000'));
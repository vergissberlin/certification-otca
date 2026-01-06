from flask import Flask
from opentelemetry import trace, metrics
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor, OTLPSpanExporter
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
from opentelemetry.exporter.otlp.proto.grpc.metric_exporter import OTLPMetricExporter

app = Flask(__name__)

trace.set_tracer_provider(TracerProvider(resource=Resource.create({"service.name": "service-python"})))
tracer = trace.get_tracer(__name__)
span_processor = BatchSpanProcessor(OTLPSpanExporter())
trace.get_tracer_provider().add_span_processor(span_processor)
FlaskInstrumentor().instrument_app(app)

reader = PeriodicExportingMetricReader(OTLPMetricExporter())
metrics.set_meter_provider(MeterProvider(metric_readers=[reader]))
meter = metrics.get_meter("service-python-meter")
counter = meter.create_counter("requests_total")

@app.route("/hello")
def hello():
    with tracer.start_as_current_span("hello-span"):
        counter.add(1)
        return "Hello from Python Service!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
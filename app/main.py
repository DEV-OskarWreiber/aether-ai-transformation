from fastapi import FastAPI, Depends, HTTPException
from .core.engine import ImpactEngine
from .core.models import TransformationInput

app = FastAPI(
    title="Aether: AI Transformation Orchestrator",
    version="1.0.0",
    description="Enterprise-scale impact analysis and AI governance orchestrator."
)

engine = ImpactEngine()

@app.get("/health")
async def health():
    return {"status": "operational", "engine": "ready"}

@app.post("/analyze/impact")
async def analyze_impact(data: TransformationInput):
    try:
        results = engine.calculate_transformation_roi(data)
        return {"impact_analysis": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)

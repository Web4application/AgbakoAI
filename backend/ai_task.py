async def healthcare_predict_treatment(symptom: str):
    # This is where your AI model logic lives
    if "fever" in symptom.lower():
        return {"treatment": "Take ibuprofen and rest"}
    return {"treatment": "Consult a doctor"}

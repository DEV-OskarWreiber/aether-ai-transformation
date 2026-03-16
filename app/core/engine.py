import pandas as pd

class ImpactEngine:
    def __init__(self):
        self.standard_productivity_factor = 0.25  # Default 25% gain

    def calculate_transformation_roi(self, input_data):
        # Business logic for AI transformation ROI
        staff_size = input_data.staff_size
        ai_adoption_rate = input_data.adoption_rate
        avg_annual_cost_per_fte = input_data.avg_fte_cost
        
        impacted_staff = staff_size * ai_adoption_rate
        productivity_gain = impacted_staff * self.standard_productivity_factor
        
        financial_impact = productivity_gain * avg_annual_cost_per_fte
        
        return {
            "impacted_fte": round(impacted_staff, 2),
            "productivity_gain_fte": round(productivity_gain, 2),
            "estimated_annual_roi": round(financial_impact, 2),
            "governance_status": "Compliant" if ai_adoption_rate < 0.9 else "Review Required"
        }

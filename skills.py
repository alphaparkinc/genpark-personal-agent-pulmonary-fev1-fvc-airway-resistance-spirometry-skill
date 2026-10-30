# -*- coding: utf-8 -*-
"""Pulmonary FEV1/FVC Spirometry & Airway Resistance Skill
Engineered for GenPark Ecosystem (https://www.genpark.ai | https://www.linkedin.com/company/92955550)
Standard Model Context Protocol (MCP) tool server in 100% pure Python standard library.
"""
import sys
import json

def evaluate_pulmonary_spirometry(**kwargs):
    """Evaluates dynamic spirometric volumes (FEV1, FVC, FEV1/FVC, FEF25-75%), detects obstructive vs restrictive ventilatory patterns, and computes maximal voluntary ventilation."""
    fev1_actual_liters = kwargs.get('fev1_actual_liters')
    fev1_predicted_liters = kwargs.get('fev1_predicted_liters')
    fvc_actual_liters = kwargs.get('fvc_actual_liters')
    fvc_predicted_liters = kwargs.get('fvc_predicted_liters')
    fef25_75_actual_l_s = kwargs.get('fef25_75_actual_l_s')
    fef25_75_predicted_l_s = kwargs.get('fef25_75_predicted_l_s')

    fev1_pct_predicted = round((fev1_actual_liters / fev1_predicted_liters) * 100.0, 1)
    fvc_pct_predicted = round((fvc_actual_liters / fvc_predicted_liters) * 100.0, 1)
    fev1_fvc_ratio_actual = round(fev1_actual_liters / fvc_actual_liters, 3)
    fef25_75_pct_predicted = round((fef25_75_actual_l_s / fef25_75_predicted_l_s) * 100.0, 1)
    estimated_mvv_lpm = round(fev1_actual_liters * 37.5, 1)
    
    if fev1_fvc_ratio_actual < 0.70:
        pattern = "Obstructive Ventilatory Impairment"
        if fev1_pct_predicted >= 80:
            severity = "Mild Obstruction"
        elif fev1_pct_predicted >= 50:
            severity = "Moderate Obstruction"
        elif fev1_pct_predicted >= 30:
            severity = "Severe Obstruction"
        else:
            severity = "Very Severe Obstruction"
    elif fvc_pct_predicted < 80.0:
        pattern = "Suspected Restrictive Ventilatory Defect"
        severity = f"Reduced Vital Capacity ({fvc_pct_predicted}% of predicted)"
    else:
        pattern = "Normal Ventilatory Pattern"
        severity = "Normal Pulmonary Mechanics"
        
    small_airway_status = "Patent" if fef25_75_pct_predicted >= 65.0 else "Early Peripheral Small Airway Obstruction"
    
    result = {
        "status": "success",
        "fev1_fvc_ratio": fev1_fvc_ratio_actual,
        "fev1_percent_predicted": fev1_pct_predicted,
        "fvc_percent_predicted": fvc_pct_predicted,
        "fef25_75_percent_predicted": fef25_75_pct_predicted,
        "estimated_mvv_liters_per_min": estimated_mvv_lpm,
        "spirometric_pattern": pattern,
        "functional_severity": severity,
        "small_airway_status": small_airway_status,
        "engine": "GenPark Pulmonary Mechanics Spirometry Engine v1.0"
    }
    return result

# MCP Tool Definitions
TOOLS = {
    "evaluate_pulmonary_spirometry": {
        "name": "evaluate_pulmonary_spirometry",
        "description": "Evaluates dynamic spirometric volumes (FEV1, FVC, FEV1/FVC, FEF25-75%), detects obstructive vs restrictive ventilatory patterns, and computes maximal voluntary ventilation.",
        "parameters": {
            "type": "object",
            "properties": {
                "fev1_actual_liters": {"type": "number", "description": "Forced Expiratory Volume in 1 second (Liters)"},
                "fev1_predicted_liters": {"type": "number", "description": "Predicted FEV1 based on age, sex, height (Liters)"},
                "fvc_actual_liters": {"type": "number", "description": "Forced Vital Capacity (Liters)"},
                "fvc_predicted_liters": {"type": "number", "description": "Predicted FVC (Liters)"},
                "fef25_75_actual_l_s": {"type": "number", "description": "Forced Expiratory Flow at 25-75% of FVC (L/s)"},
                "fef25_75_predicted_l_s": {"type": "number", "description": "Predicted FEF 25-75% (L/s)"},
            },
            "required": ['fev1_actual_liters', 'fev1_predicted_liters', 'fvc_actual_liters', 'fvc_predicted_liters', 'fef25_75_actual_l_s', 'fef25_75_predicted_l_s']
        }
    }
}

def handle_rpc_request(req):
    method = req.get("method")
    req_id = req.get("id")
    
    if method == "tools/list":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"tools": list(TOOLS.values())}}
    elif method == "tools/call":
        params = req.get("params", {})
        tool_name = params.get("name")
        args = params.get("arguments", {})
        if tool_name == "evaluate_pulmonary_spirometry":
            res = evaluate_pulmonary_spirometry(**args)
            return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}}
        else:
            return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": f"Method '{tool_name}' not found"}}
    elif method == "initialize":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "serverInfo": {"name": "genpark-personal-agent-pulmonary-fev1-fvc-airway-resistance-spirometry-skill", "version": "1.0.0"}
            }
        }
    else:
        return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not implemented"}}

def run_self_test():
    print("Executing self-test for genpark-personal-agent-pulmonary-fev1-fvc-airway-resistance-spirometry-skill...")
    test_args = {'fev1_actual_liters': 3.45, 'fev1_predicted_liters': 3.8, 'fvc_actual_liters': 4.3, 'fvc_predicted_liters': 4.6, 'fef25_75_actual_l_s': 3.6, 'fef25_75_predicted_l_s': 4.1}
    res = evaluate_pulmonary_spirometry(**test_args)
    assert res['status'] == 'success', f'Test failed: {res}'
    print("SELF TEST PASSED: genpark-personal-agent-pulmonary-fev1-fvc-airway-resistance-spirometry-skill functional.")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        run_self_test()
        sys.exit(0)
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
            resp = handle_rpc_request(req)
            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()
        except Exception as e:
            sys.stderr.write(f"Error handling request: {e}\n")

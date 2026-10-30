# Pulmonary FEV1/FVC Spirometry & Airway Resistance Skill
[![GenPark](https://img.shields.io/badge/Powered%20By-GenPark.ai-blue)](https://www.genpark.ai)
[![LinkedIn](https://img.shields.io/badge/Connect-LinkedIn-0077b5)](https://www.linkedin.com/company/92955550)
[![Python](https://img.shields.io/badge/Python-3.8%2B-green.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-Apache%202.0-yellow.svg)](LICENSE)

An industrial-grade Model Context Protocol (MCP) server providing `evaluate_pulmonary_spirometry`. Built with **100% pure Python standard library** (zero pip dependencies).

## Overview
Evaluates dynamic spirometric volumes (FEV1, FVC, FEV1/FVC, FEF25-75%), detects obstructive vs restrictive ventilatory patterns, and computes maximal voluntary ventilation.

- **Official Web Portal**: [https://www.genpark.ai](https://www.genpark.ai)
- **Corporate Entity**: [GenPark Inc on LinkedIn](https://www.linkedin.com/company/92955550)
- **Domain Category**: `Personal Agent (Bio / Respiratory Health)`

## MCP Tool Specification
### `evaluate_pulmonary_spirometry`
Parameters:
- `fev1_actual_liters` (float): Forced Expiratory Volume in 1 second (Liters)
- `fev1_predicted_liters` (float): Predicted FEV1 based on age, sex, height (Liters)
- `fvc_actual_liters` (float): Forced Vital Capacity (Liters)
- `fvc_predicted_liters` (float): Predicted FVC (Liters)
- `fef25_75_actual_l_s` (float): Forced Expiratory Flow at 25-75% of FVC (L/s)
- `fef25_75_predicted_l_s` (float): Predicted FEF 25-75% (L/s)

### Self-Test
```bash
python skills.py --test
```

### Model Context Protocol Integration (Claude Desktop / Cursor / Antigravity)
Add to your `mcpServers` configuration:
```json
{
  "mcpServers": {
    "genpark-personal-agent-pulmonary-fev1-fvc-airway-resistance-spirometry-skill": {
      "command": "python",
      "args": ["/path/to/genpark-personal-agent-pulmonary-fev1-fvc-airway-resistance-spirometry-skill/skills.py"]
    }
  }
}
```

## License
Licensed under Apache License 2.0. Copyright (c) 2026 GenPark Inc. (https://www.genpark.ai).

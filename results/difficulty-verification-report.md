# Difficulty Verification Report

## 1. Tier-Level Baseline Summary

| Tier | Agents | Mean | Min | Max | Expected Range | Status |
|------|--------|------|-----|-----|----------------|--------|
| EASY | 6 | 37.2% | 33.3% | 50.0% | 30-40% | IN RANGE |
| MEDIUM | 8 | 57.1% | 40.0% | 66.7% | 50-60% | IN RANGE |
| HARD | 7 | 69.5% | 60.0% | 83.3% | 70-80% | OUT OF RANGE |

## 2. Delta Comparison

| Agent | Tier | Baseline | Optimized | Delta | Expected | Match |
|-------|------|----------|-----------|-------|----------|-------|
| compliance_risk/audit_trail_reviewer | medium | 50.0% | 100.0% | +50.0% | 20-30% | **NO** |
| compliance_risk/data_privacy_officer | medium | 66.7% | 80.0% | +13.3% | 20-30% | **NO** |
| compliance_risk/regulatory_compliance_checker | hard | 60.0% | 75.0% | +15.0% | 10-20% | YES |
| compliance_risk/security_incident_responder | hard | 66.7% | 83.3% | +16.6% | 10-20% | YES |
| customer_sales/account_manager | hard | 75.0% | 100.0% | +25.0% | 10-20% | **NO** |
| customer_sales/customer_support | medium | 66.7% | 75.0% | +8.3% | 20-30% | **NO** |
| customer_sales/deal_pipeline | medium | 40.0% | 83.3% | +43.3% | 20-30% | **NO** |
| customer_sales/lead_qualifier | easy | 33.3% | 66.7% | +33.4% | 30-50% | YES |
| finance_procurement/procurement_agent | hard | 66.7% | 100.0% | +33.3% | 10-20% | **NO** |
| hr_people_ops/employee_directory | easy | 33.3% | 66.7% | +33.4% | 30-50% | YES |
| hr_people_ops/leave_manager | medium | 50.0% | 83.3% | +33.3% | 20-30% | **NO** |
| hr_people_ops/onboarding_coordinator | hard | 60.0% | 100.0% | +40.0% | 10-20% | **NO** |
| hr_people_ops/payroll_processor | medium | 50.0% | 75.0% | +25.0% | 20-30% | YES |
| it_service_mgmt/access_provisioner | easy | 33.3% | 75.0% | +41.7% | 30-50% | YES |
| it_service_mgmt/incident_commander | medium | 66.7% | 80.0% | +13.3% | 20-30% | **NO** |
| it_service_mgmt/password_reset_agent | easy | 50.0% | 66.7% | +16.7% | 30-50% | **NO** |
| it_service_mgmt/service_desk_agent | hard | 75.0% | 80.0% | +5.0% | 10-20% | **NO** |
| supply_chain/inventory_tracker | easy | 40.0% | 100.0% | +60.0% | 30-50% | **NO** |
| supply_chain/order_fulfillment | medium | 66.7% | 83.3% | +16.6% | 20-30% | **NO** |
| supply_chain/shipping_coordinator | easy | 33.3% | 75.0% | +41.7% | 30-50% | YES |
| supply_chain/vendor_manager | hard | 83.3% | 100.0% | +16.7% | 10-20% | YES |

## 3. Delta Ordering Check

- EASY mean delta: 37.8%
- MEDIUM mean delta: 25.4%
- HARD mean delta: 21.7%

**PASS**: EASY delta > MEDIUM delta > HARD delta — difficulty classifications are validated.

## 4. Reclassification Analysis

| Agent | Current Tier | Baseline | Triggers | Recommendation |
|-------|-------------|----------|----------|----------------|
| compliance_risk/audit_trail_reviewer | medium | 50.0% | Delta 50.0% far outside expected 20-30% | Review needed |
| customer_sales/customer_support | medium | 66.7% | Delta 8.3% far outside expected 20-30% | Review needed |
| customer_sales/deal_pipeline | medium | 40.0% | Delta 43.3% far outside expected 20-30% | Review needed |
| finance_procurement/procurement_agent | hard | 66.7% | Delta 33.3% far outside expected 10-20% | Review needed |
| hr_people_ops/onboarding_coordinator | hard | 60.0% | Delta 40.0% far outside expected 10-20% | Review needed |
| it_service_mgmt/password_reset_agent | easy | 50.0% | Delta 16.7% far outside expected 30-50% | Review needed |

## 5. Conclusion

While delta ordering is correct, some individual agents show baseline rates outside expected ranges. These agents should be reviewed for potential reclassification.
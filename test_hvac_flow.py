from mcp_server import process_hvac_compliance

def test_hvac_flow():
    print("Testing HVAC AI Micro-SaaS Flow...")
    
    # Sample base64 (placeholder)
    sample_b64 = "dGVzdC1pbWFnZS1kYXRh" 
    
    result = process_hvac_compliance(sample_b64)
    print("\n--- Result ---\n")
    print(result)
    print("\n--------------\n")
    
    if "✅ COMPLIANT" in result and "Carrier" in result:
        print("Verification Successful!")
    else:
        print("Verification Failed or Unexpected Output.")

if __name__ == "__main__":
    test_hvac_flow()

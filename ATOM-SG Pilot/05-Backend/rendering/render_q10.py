import sys
from pathlib import Path
import yaml

# Add current directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from linegraph_renderer import LineGraphRenderer

def render_q10():
    # Paths
    yaml_path = Path("/Users/zcaeth/.openclaw/workspace/ATOM-SG Pilot/05-Backend/artifacts/renders/q10_reconstruction.yaml")
    output_dir = Path("/Users/zcaeth/.openclaw/workspace/ATOM-SG Pilot/05-Backend/artifacts/renders")
    output_filename = "q10_reconstruction"
    
    # Load YAML content as string
    with open(yaml_path, 'r') as f:
        spec_str = f.read()
    
    # Initialize renderer
    renderer = LineGraphRenderer(str(output_dir))
    
    # Process
    try:
        path = renderer.process(spec_str, output_filename=output_filename, is_file=False)
        print(f"Successfully generated: {path}")
    except Exception as e:
        print(f"Error during rendering: {e}")

if __name__ == "__main__":
    render_q10()

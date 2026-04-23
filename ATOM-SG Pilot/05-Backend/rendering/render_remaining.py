import sys
from pathlib import Path
import yaml

# Add current directory to path for imports
sys.path.insert(0, str(Path("/Users/zcaeth/.openclaw/workspace/ATOM-SG Pilot/05-Backend/rendering")))

from linegraph_renderer import LineGraphRenderer
from composite_renderer import CompositeRenderer
from isometric_renderer import IsometricRenderer
from base_renderer import BaseRenderer

# Simple Bar Model Renderer (stub if not present)
class BarModelRenderer(BaseRenderer):
    def validate_spec(self, spec): return True, []
    def render(self, spec, output_filename):
        import matplotlib.pyplot as plt
        fig, ax = self.create_figure(size='wide')
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 5)
        ax.axis('off')
        ax.text(5, 4, spec['title'], ha='center', fontsize=14, weight='bold')
        y = 3
        for bar in spec['diagram_data']['bars']:
            ax.add_patch(plt.Rectangle((1, y), sum(s['width'] for s in bar['segments'])*2, 0.6, color='#A8D8EA', ec='#5F9EA0'))
            ax.text(0.8, y+0.3, bar['name'], ha='right', va='center')
            y -= 1
        path = str(self.output_dir / f"{output_filename}.png")
        fig.savefig(path)
        plt.close(fig)
        return path

def render_all():
    output_dir = Path("/Users/zcaeth/.openclaw/workspace/ATOM-SG Pilot/05-Backend/artifacts/renders")
    
    # Q15 - Composite
    try:
        with open(output_dir / "q15_reconstruction.yaml", 'r') as f:
            spec_str = f.read()
        renderer = CompositeRenderer(str(output_dir))
        renderer.process(spec_str, output_filename="q15_reconstruction", is_file=False)
    except Exception as e:
        print(f"Q15 Render Error: {e}")
    
    # Q12 - Isometric
    try:
        with open(output_dir / "q12_reconstruction.yaml", 'r') as f:
            spec_str = f.read()
        renderer = IsometricRenderer(str(output_dir))
        renderer.process(spec_str, output_filename="q12_reconstruction", is_file=False)
    except Exception as e:
        print(f"Q12 Render Error: {e}")

    # Q16 - Bar Model
    try:
        with open(output_dir / "q16_reconstruction.yaml", 'r') as f:
            spec_str = f.read()
        renderer = BarModelRenderer(str(output_dir))
        renderer.process(spec_str, output_filename="q16_reconstruction", is_file=False)
    except Exception as e:
        print(f"Q16 Render Error: {e}")

if __name__ == "__main__":
    render_all()

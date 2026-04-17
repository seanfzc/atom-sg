// Canvas Annotation Module
// Handles diagram drawing and annotations
// P0 Fix #6: Added text annotations, expanded color palette, undo/redo stack

class CanvasAnnotation {
    constructor() {
        this.canvas = document.getElementById('annotation-canvas');
        this.ctx = null;
        this.isDrawing = false;
        this.currentTool = 'pen';
        this.currentColor = '#2563eb';
        this.currentLineWidth = 2;
        this.startX = 0;
        this.startY = 0;
        this.annotations = [];
        
        // P0 Fix #6: Expanded color palette
        this.colorPalette = [
            '#2563eb', // Blue (default)
            '#dc2626', // Red
            '#16a34a', // Green
            '#9333ea', // Purple
            '#ea580c', // Orange
            '#0891b2', // Cyan
            '#000000', // Black
            '#6b7280', // Gray
            '#fbbf24', // Yellow
            '#ec4899'  // Pink
        ];
        
        // P0 Fix #6: Undo/Redo stacks
        this.undoStack = [];
        this.redoStack = [];
        this.maxUndoLevels = 50;
        
        // P0 Fix #6: Text annotation mode
        this.textMode = false;
        this.textPosition = null;
        
        this.init();
    }

    init() {
        if (!this.canvas) return;
        
        this.ctx = this.canvas.getContext('2d');
        this.setupCanvas();
        this.setupEventListeners();
        this.setupToolButtons();
    }

    setupCanvas() {
        // Set canvas size
        const container = this.canvas.parentElement;
        const rect = container.getBoundingClientRect();
        
        this.canvas.width = rect.width;
        this.canvas.height = 400;
        
        // Set default styles
        this.ctx.lineCap = 'round';
        this.ctx.lineJoin = 'round';
        this.ctx.strokeStyle = this.currentColor;
        this.ctx.lineWidth = this.currentLineWidth;
        
        // Fill with white background
        this.ctx.fillStyle = 'white';
        this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);
        
        // Handle resize
        window.addEventListener('resize', () => {
            this.saveAnnotations();
            this.setupCanvas();
            this.restoreAnnotations();
        });
    }

    setupEventListeners() {
        // Mouse events
        this.canvas.addEventListener('mousedown', (e) => this.startDrawing(e));
        this.canvas.addEventListener('mousemove', (e) => this.draw(e));
        this.canvas.addEventListener('mouseup', () => this.stopDrawing());
        this.canvas.addEventListener('mouseout', () => this.stopDrawing());
        
        // Touch events
        this.canvas.addEventListener('touchstart', (e) => {
            e.preventDefault();
            const touch = e.touches[0];
            this.startDrawing(touch);
        });
        this.canvas.addEventListener('touchmove', (e) => {
            e.preventDefault();
            const touch = e.touches[0];
            this.draw(touch);
        });
        this.canvas.addEventListener('touchend', () => this.stopDrawing());
    }

    setupToolButtons() {
        const toolButtons = document.querySelectorAll('.tool-btn');
        
        toolButtons.forEach(btn => {
            btn.addEventListener('click', () => {
                const tool = btn.dataset.tool;
                
                if (tool === 'clear') {
                    this.clearCanvas();
                } else if (tool === 'undo') {
                    this.undo();
                } else if (tool === 'redo') {
                    this.redo();
                } else if (tool === 'text') {
                    this.setTool('text');
                    toolButtons.forEach(b => b.classList.remove('active'));
                    btn.classList.add('active');
                } else {
                    this.setTool(tool);
                    toolButtons.forEach(b => b.classList.remove('active'));
                    btn.classList.add('active');
                }
            });
        });
        
        // P0 Fix #6: Setup color palette
        this.setupColorPalette();
        
        // Set pen as default tool
        this.setTool('pen');
        document.querySelector('.tool-btn[data-tool="pen"]').classList.add('active');
    }

    // P0 Fix #6: Setup expanded color palette
    setupColorPalette() {
        const paletteContainer = document.getElementById('color-palette');
        if (!paletteContainer) return;
        
        paletteContainer.innerHTML = this.colorPalette.map((color, index) => `
            <button class="color-btn ${index === 0 ? 'active' : ''}" 
                    data-color="${color}" 
                    style="background-color: ${color};"
                    title="Color: ${color}">
            </button>
        `).join('');
        
        paletteContainer.querySelectorAll('.color-btn').forEach(btn => {
            btn.addEventListener('click', () => {
                const color = btn.dataset.color;
                this.currentColor = color;
                this.ctx.strokeStyle = color;
                this.ctx.fillStyle = color;
                
                paletteContainer.querySelectorAll('.color-btn').forEach(b => b.classList.remove('active'));
                btn.classList.add('active');
            });
        });
    }

    setTool(tool) {
        this.currentTool = tool;
        this.textMode = (tool === 'text');
        
        switch (tool) {
            case 'pen':
                this.currentLineWidth = 2;
                break;
            case 'line':
                this.currentLineWidth = 3;
                break;
            case 'eraser':
                this.currentColor = 'white';
                this.currentLineWidth = 20;
                break;
            case 'text':
                // Text tool - will show input dialog on click
                this.currentLineWidth = 2;
                break;
        }
        
        this.ctx.strokeStyle = this.currentColor;
        this.ctx.lineWidth = this.currentLineWidth;
        this.ctx.fillStyle = this.currentColor;
    }

    // P0 Fix #6: Add text annotation
    addTextAnnotation(x, y) {
        const text = prompt('Enter text annotation:', '');
        if (text && text.trim()) {
            const fontSize = 14;
            this.ctx.font = `${fontSize}px Arial`;
            this.ctx.fillStyle = this.currentColor;
            this.ctx.fillText(text, x, y);
            
            // Save to annotations
            this.saveState(); // Save current state before adding
            
            this.annotations.push({
                type: 'text',
                text: text,
                x: x,
                y: y,
                color: this.currentColor,
                fontSize: fontSize
            });
            
            this.saveState(); // Save state after adding
        }
    }

    // P0 Fix #6: Undo last action
    undo() {
        if (this.undoStack.length > 0) {
            const lastState = this.undoStack.pop();
            this.redoStack.push(this.getCurrentState());
            this.restoreState(lastState);
        }
    }

    // P0 Fix #6: Redo last undone action
    redo() {
        if (this.redoStack.length > 0) {
            const nextState = this.redoStack.pop();
            this.undoStack.push(this.getCurrentState());
            this.restoreState(nextState);
        }
    }

    // P0 Fix #6: Get current canvas state
    getCurrentState() {
        return {
            imageData: this.ctx.getImageData(0, 0, this.canvas.width, this.canvas.height),
            annotations: JSON.parse(JSON.stringify(this.annotations))
        };
    }

    // P0 Fix #6: Save current state to undo stack
    saveState() {
        const state = this.getCurrentState();
        this.undoStack.push(state);
        
        // Limit undo stack size
        if (this.undoStack.length > this.maxUndoLevels) {
            this.undoStack.shift();
        }
        
        // Clear redo stack when new action is performed
        this.redoStack = [];
    }

    // P0 Fix #6: Restore canvas state
    restoreState(state) {
        this.ctx.putImageData(state.imageData, 0, 0);
        this.annotations = state.annotations;
    }

    getCanvasCoordinates(e) {
        const rect = this.canvas.getBoundingClientRect();
        return {
            x: e.clientX - rect.left,
            y: e.clientY - rect.top
        };
    }

    startDrawing(e) {
        const coords = this.getCanvasCoordinates(e);
        
        // P0 Fix #6: Handle text annotation click
        if (this.textMode) {
            this.addTextAnnotation(coords.x, coords.y);
            return;
        }
        
        this.isDrawing = true;
        this.startX = coords.x;
        this.startY = coords.y;
        
        // P0 Fix #6: Save state before drawing (for undo)
        if (this.currentTool !== 'eraser') {
            this.saveState();
        }
        
        if (this.currentTool === 'pen' || this.currentTool === 'eraser') {
            this.ctx.beginPath();
            this.ctx.moveTo(coords.x, coords.y);
            
            // Add annotation
            this.annotations.push({
                type: 'point',
                x: coords.x,
                y: coords.y,
                tool: this.currentTool,
                color: this.currentColor,
                lineWidth: this.currentLineWidth
            });
        }
    }

    draw(e) {
        if (!this.isDrawing) return;
        
        const coords = this.getCanvasCoordinates(e);
        
        if (this.currentTool === 'pen' || this.currentTool === 'eraser') {
            this.ctx.lineTo(coords.x, coords.y);
            this.ctx.stroke();
            
            // Add annotation
            this.annotations.push({
                type: 'point',
                x: coords.x,
                y: coords.y,
                tool: this.currentTool,
                color: this.currentColor,
                lineWidth: this.currentLineWidth
            });
        } else if (this.currentTool === 'line') {
            // For line tool, we need to redraw the canvas each time
            this.restoreAnnotations();
            
            // Draw current line preview
            this.ctx.strokeStyle = this.currentColor;
            this.ctx.lineWidth = this.currentLineWidth;
            this.ctx.beginPath();
            this.ctx.moveTo(this.startX, this.startY);
            this.ctx.lineTo(coords.x, coords.y);
            this.ctx.stroke();
        }
    }

    stopDrawing() {
        if (!this.isDrawing) return;
        
        if (this.currentTool === 'line') {
            // P0 Fix #6: Save state before adding line
            this.saveState();
            
            // Add final line annotation
            const currentCoords = this.getCanvasCoordinates(event);
            this.annotations.push({
                type: 'line',
                startX: this.startX,
                startY: this.startY,
                endX: currentCoords.x,
                endY: currentCoords.y,
                color: this.currentColor,
                lineWidth: this.currentLineWidth
            });
            
            this.restoreAnnotations();
            
            // P0 Fix #6: Save state after adding line
            this.saveState();
        }
        
        this.isDrawing = false;
    }

    saveAnnotations() {
        // Save canvas data URL
        return this.canvas.toDataURL('image/png');
    }

    restoreAnnotations() {
        // Clear canvas
        this.ctx.fillStyle = 'white';
        this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);
        
        // Redraw all annotations
        let lastPoint = null;
        
        this.annotations.forEach(annotation => {
            this.ctx.strokeStyle = annotation.color;
            this.ctx.lineWidth = annotation.lineWidth;
            
            if (annotation.type === 'point') {
                if (lastPoint && annotation.tool === lastPoint.tool) {
                    this.ctx.beginPath();
                    this.ctx.moveTo(lastPoint.x, lastPoint.y);
                    this.ctx.lineTo(annotation.x, annotation.y);
                    this.ctx.stroke();
                }
                lastPoint = annotation;
            } else if (annotation.type === 'line') {
                this.ctx.beginPath();
                this.ctx.moveTo(annotation.startX, annotation.startY);
                this.ctx.lineTo(annotation.endX, annotation.endY);
                this.ctx.stroke();
                lastPoint = null;
            }
        });
    }

    clearCanvas() {
        // P0 Fix #6: Save state before clearing
        this.saveState();
        
        this.ctx.fillStyle = 'white';
        this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);
        this.annotations = [];
    }

    getAnnotations() {
        return this.annotations;
    }
}

// Initialize canvas when DOM is ready
let canvasAnnotation;
document.addEventListener('DOMContentLoaded', () => {
    canvasAnnotation = new CanvasAnnotation();
    window.canvasAnnotation = canvasAnnotation; // Make it globally accessible
});

// ModelCanvas.js - Interactive Model Drawing Component
// Supports bar models, unit models, comparison models, and before-after visualizations

class ModelCanvas {
    constructor(canvasId, options = {}) {
        this.canvas = document.getElementById(canvasId);
        if (!this.canvas) {
            console.error(`Canvas with id '${canvasId}' not found`);
            return;
        }
        
        this.ctx = this.canvas.getContext('2d');
        this.options = {
            width: options.width || 800,
            height: options.height || 600,
            backgroundColor: options.backgroundColor || '#ffffff',
            gridSize: options.gridSize || 20,
            showGrid: options.showGrid !== false,
            snapToGrid: options.snapToGrid !== false,
            ...options
        };
        
        // Set canvas size
        this.canvas.width = this.options.width;
        this.canvas.height = this.options.height;
        this.canvas.style.width = '100%';
        this.canvas.style.height = 'auto';
        
        // Drawing state
        this.elements = [];
        this.selectedElement = null;
        this.isDrawing = false;
        this.currentTool = 'select';
        this.currentColor = '#3b82f6';
        this.currentFillColor = '#dbeafe';
        this.strokeWidth = 2;
        
        // History for undo/redo
        this.history = [];
        this.historyIndex = -1;
        this.maxHistory = 50;
        
        // Event handlers
        this.setupEventListeners();
        
        // Initial render
        this.saveState();
        this.render();
    }
    
    setupEventListeners() {
        let startX, startY;
        
        this.canvas.addEventListener('mousedown', (e) => {
            const rect = this.canvas.getBoundingClientRect();
            startX = (e.clientX - rect.left) * (this.canvas.width / rect.width);
            startY = (e.clientY - rect.top) * (this.canvas.height / rect.height);
            
            if (this.options.snapToGrid) {
                startX = Math.round(startX / this.options.gridSize) * this.options.gridSize;
                startY = Math.round(startY / this.options.gridSize) * this.options.gridSize;
            }
            
            this.handleMouseDown(startX, startY);
        });
        
        this.canvas.addEventListener('mousemove', (e) => {
            const rect = this.canvas.getBoundingClientRect();
            let x = (e.clientX - rect.left) * (this.canvas.width / rect.width);
            let y = (e.clientY - rect.top) * (this.canvas.height / rect.height);
            
            if (this.options.snapToGrid) {
                x = Math.round(x / this.options.gridSize) * this.options.gridSize;
                y = Math.round(y / this.options.gridSize) * this.options.gridSize;
            }
            
            this.handleMouseMove(x, y, startX, startY);
        });
        
        this.canvas.addEventListener('mouseup', (e) => {
            const rect = this.canvas.getBoundingClientRect();
            let x = (e.clientX - rect.left) * (this.canvas.width / rect.width);
            let y = (e.clientY - rect.top) * (this.canvas.height / rect.height);
            
            if (this.options.snapToGrid) {
                x = Math.round(x / this.options.gridSize) * this.options.gridSize;
                y = Math.round(y / this.options.gridSize) * this.options.gridSize;
            }
            
            this.handleMouseUp(x, y);
        });
        
        // Touch support
        this.canvas.addEventListener('touchstart', (e) => {
            e.preventDefault();
            const touch = e.touches[0];
            const rect = this.canvas.getBoundingClientRect();
            startX = (touch.clientX - rect.left) * (this.canvas.width / rect.width);
            startY = (touch.clientY - rect.top) * (this.canvas.height / rect.height);
            this.handleMouseDown(startX, startY);
        });
        
        this.canvas.addEventListener('touchmove', (e) => {
            e.preventDefault();
            const touch = e.touches[0];
            const rect = this.canvas.getBoundingClientRect();
            let x = (touch.clientX - rect.left) * (this.canvas.width / rect.width);
            let y = (touch.clientY - rect.top) * (this.canvas.height / rect.height);
            this.handleMouseMove(x, y, startX, startY);
        });
        
        this.canvas.addEventListener('touchend', (e) => {
            this.handleMouseUp(startX, startY);
        });
    }
    
    handleMouseDown(x, y) {
        this.isDrawing = true;
        
        if (this.currentTool === 'select') {
            this.selectedElement = this.getElementAt(x, y);
            if (this.selectedElement) {
                this.selectedElement.offsetX = x - this.selectedElement.x;
                this.selectedElement.offsetY = y - this.selectedElement.y;
            }
        } else if (this.currentTool === 'bar') {
            this.tempElement = {
                type: 'bar',
                x: x,
                y: y,
                width: 0,
                height: 40,
                color: this.currentColor,
                fillColor: this.currentFillColor,
                label: ''
            };
        } else if (this.currentTool === 'unit') {
            this.addUnit(x, y);
        } else if (this.currentTool === 'label') {
            this.addLabel(x, y);
        } else if (this.currentTool === 'arrow') {
            this.tempElement = {
                type: 'arrow',
                x1: x,
                y1: y,
                x2: x,
                y2: y,
                color: this.currentColor
            };
        } else if (this.currentTool === 'bracket') {
            this.tempElement = {
                type: 'bracket',
                x1: x,
                y1: y,
                x2: x,
                y2: y,
                color: this.currentColor
            };
        }
    }
    
    handleMouseMove(x, y, startX, startY) {
        if (!this.isDrawing) return;
        
        if (this.currentTool === 'select' && this.selectedElement) {
            this.selectedElement.x = x - this.selectedElement.offsetX;
            this.selectedElement.y = y - this.selectedElement.offsetY;
            this.render();
        } else if (this.tempElement) {
            if (this.currentTool === 'bar') {
                this.tempElement.width = x - this.tempElement.x;
            } else if (this.currentTool === 'arrow' || this.currentTool === 'bracket') {
                this.tempElement.x2 = x;
                this.tempElement.y2 = y;
            }
            this.render();
            this.drawTempElement();
        }
    }
    
    handleMouseUp(x, y) {
        if (!this.isDrawing) return;
        this.isDrawing = false;
        
        if (this.tempElement) {
            // Validate minimum size
            if (this.currentTool === 'bar' && Math.abs(this.tempElement.width) >= 20) {
                // Normalize bar direction
                if (this.tempElement.width < 0) {
                    this.tempElement.x += this.tempElement.width;
                    this.tempElement.width = Math.abs(this.tempElement.width);
                }
                this.elements.push({...this.tempElement});
                this.saveState();
            } else if ((this.currentTool === 'arrow' || this.currentTool === 'bracket') && 
                       (Math.abs(this.tempElement.x2 - this.tempElement.x1) > 10 || 
                        Math.abs(this.tempElement.y2 - this.tempElement.y1) > 10)) {
                this.elements.push({...this.tempElement});
                this.saveState();
            }
            this.tempElement = null;
            this.render();
        } else if (this.currentTool === 'select' && this.selectedElement) {
            this.saveState();
        }
    }
    
    getElementAt(x, y) {
        // Search in reverse order (top to bottom)
        for (let i = this.elements.length - 1; i >= 0; i--) {
            const el = this.elements[i];
            if (this.hitTest(el, x, y)) {
                return el;
            }
        }
        return null;
    }
    
    hitTest(element, x, y) {
        if (element.type === 'bar') {
            return x >= element.x && x <= element.x + element.width &&
                   y >= element.y && y <= element.y + element.height;
        } else if (element.type === 'unit') {
            const dx = x - element.x;
            const dy = y - element.y;
            return dx * dx + dy * dy <= (element.size / 2) ** 2;
        } else if (element.type === 'label') {
            const metrics = this.ctx.measureText(element.text);
            return x >= element.x && x <= element.x + metrics.width &&
                   y >= element.y - 12 && y <= element.y + 4;
        } else if (element.type === 'arrow' || element.type === 'bracket') {
            // Simple line hit test
            const dist = this.pointToLineDistance(x, y, element.x1, element.y1, element.x2, element.y2);
            return dist < 10;
        }
        return false;
    }
    
    pointToLineDistance(px, py, x1, y1, x2, y2) {
        const A = px - x1;
        const B = py - y1;
        const C = x2 - x1;
        const D = y2 - y1;
        
        const dot = A * C + B * D;
        const lenSq = C * C + D * D;
        let param = -1;
        
        if (lenSq !== 0) {
            param = dot / lenSq;
        }
        
        let xx, yy;
        if (param < 0) {
            xx = x1;
            yy = y1;
        } else if (param > 1) {
            xx = x2;
            yy = y2;
        } else {
            xx = x1 + param * C;
            yy = y1 + param * D;
        }
        
        const dx = px - xx;
        const dy = py - yy;
        return Math.sqrt(dx * dx + dy * dy);
    }
    
    addUnit(x, y) {
        this.elements.push({
            type: 'unit',
            x: x,
            y: y,
            size: 30,
            color: this.currentColor,
            fillColor: this.currentFillColor,
            shape: 'circle' // circle, square, triangle
        });
        this.saveState();
        this.render();
    }
    
    addLabel(x, y, text = 'Label') {
        this.elements.push({
            type: 'label',
            x: x,
            y: y,
            text: text,
            color: this.currentColor,
            fontSize: 14
        });
        this.saveState();
        this.render();
    }
    
    // Template methods for common model types
    createBarModel(bars) {
        // bars: [{ label, value, color, fillColor }, ...]
        this.clear();
        const startY = 200;
        const maxValue = Math.max(...bars.map(b => b.value));
        const maxWidth = 600;
        const barHeight = 50;
        const spacing = 80;
        
        bars.forEach((bar, index) => {
            const width = (bar.value / maxValue) * maxWidth;
            this.elements.push({
                type: 'bar',
                x: 100,
                y: startY + index * spacing,
                width: width,
                height: barHeight,
                color: bar.color || this.currentColor,
                fillColor: bar.fillColor || this.currentFillColor,
                label: bar.label,
                value: bar.value
            });
            
            // Add value label
            this.elements.push({
                type: 'label',
                x: 100 + width / 2,
                y: startY + index * spacing + barHeight / 2 + 5,
                text: bar.value.toString(),
                color: '#000000',
                fontSize: 16,
                align: 'center'
            });
            
            // Add name label
            this.elements.push({
                type: 'label',
                x: 50,
                y: startY + index * spacing + barHeight / 2 + 5,
                text: bar.label,
                color: '#374151',
                fontSize: 14,
                align: 'right'
            });
        });
        
        this.saveState();
        this.render();
    }
    
    createUnitModel(units, options = {}) {
        // units: [{ count, label, color, shape }, ...]
        this.clear();
        const startX = 100;
        const startY = 200;
        const unitSize = options.unitSize || 30;
        const spacing = options.spacing || 10;
        const groupSpacing = options.groupSpacing || 60;
        
        let currentX = startX;
        
        units.forEach((group, groupIndex) => {
            // Draw group label
            this.elements.push({
                type: 'label',
                x: currentX + (group.count * (unitSize + spacing)) / 2,
                y: startY - 30,
                text: group.label,
                color: '#374151',
                fontSize: 14,
                align: 'center'
            });
            
            // Draw units
            for (let i = 0; i < group.count; i++) {
                this.elements.push({
                    type: 'unit',
                    x: currentX + i * (unitSize + spacing) + unitSize / 2,
                    y: startY + unitSize / 2,
                    size: unitSize,
                    color: group.color || this.currentColor,
                    fillColor: group.fillColor || this.currentFillColor,
                    shape: group.shape || 'circle'
                });
            }
            
            currentX += group.count * (unitSize + spacing) + groupSpacing;
        });
        
        this.saveState();
        this.render();
    }
    
    createComparisonModel(items) {
        // items: [{ label, value, color }, ...]
        this.clear();
        const startX = 100;
        const startY = 150;
        const lineLength = 500;
        const spacing = 100;
        
        // Draw base line
        this.elements.push({
            type: 'arrow',
            x1: startX,
            y1: startY + 200,
            x2: startX + lineLength,
            y2: startY + 200,
            color: '#9ca3af'
        });
        
        items.forEach((item, index) => {
            const x = startX + (item.value / 100) * lineLength;
            const y = startY + index * spacing;
            
            // Draw vertical line
            this.elements.push({
                type: 'arrow',
                x1: x,
                y1: startY + 200,
                x2: x,
                y2: y + 40,
                color: item.color || this.currentColor
            });
            
            // Draw item box
            this.elements.push({
                type: 'bar',
                x: x - 40,
                y: y,
                width: 80,
                height: 40,
                color: item.color || this.currentColor,
                fillColor: item.fillColor || this.currentFillColor,
                label: item.label
            });
            
            // Add label
            this.elements.push({
                type: 'label',
                x: x,
                y: y + 25,
                text: item.label,
                color: '#000000',
                fontSize: 12,
                align: 'center'
            });
            
            // Add value
            this.elements.push({
                type: 'label',
                x: x,
                y: startY + 220,
                text: item.value.toString(),
                color: item.color || this.currentColor,
                fontSize: 14,
                align: 'center'
            });
        });
        
        this.saveState();
        this.render();
    }
    
    createBeforeAfterModel(before, after, change) {
        // before, after, change: { value, label, color }
        this.clear();
        const centerX = this.canvas.width / 2;
        const startY = 150;
        const boxWidth = 120;
        const boxHeight = 60;
        
        // Before box
        this.elements.push({
            type: 'bar',
            x: centerX - 200,
            y: startY,
            width: boxWidth,
            height: boxHeight,
            color: before.color || '#6b7280',
            fillColor: before.fillColor || '#f3f4f6',
            label: before.label || 'Before'
        });
        
        this.elements.push({
            type: 'label',
            x: centerX - 200 + boxWidth / 2,
            y: startY + boxHeight / 2 + 5,
            text: before.value.toString(),
            color: '#000000',
            fontSize: 18,
            align: 'center'
        });
        
        this.elements.push({
            type: 'label',
            x: centerX - 200 + boxWidth / 2,
            y: startY - 20,
            text: before.label || 'Before',
            color: '#6b7280',
            fontSize: 14,
            align: 'center'
        });
        
        // Change arrow
        const isIncrease = after.value > before.value;
        const changeText = isIncrease ? `+${change.value}` : `-${change.value}`;
        const changeColor = isIncrease ? '#10b981' : '#ef4444';
        
        this.elements.push({
            type: 'arrow',
            x1: centerX - 200 + boxWidth + 20,
            y1: startY + boxHeight / 2,
            x2: centerX + 200 - 20,
            y2: startY + boxHeight / 2,
            color: changeColor,
            label: changeText
        });
        
        this.elements.push({
            type: 'label',
            x: centerX,
            y: startY + boxHeight / 2 - 15,
            text: changeText,
            color: changeColor,
            fontSize: 16,
            align: 'center'
        });
        
        // After box
        this.elements.push({
            type: 'bar',
            x: centerX + 200 - boxWidth,
            y: startY,
            width: boxWidth,
            height: boxHeight,
            color: after.color || '#3b82f6',
            fillColor: after.fillColor || '#dbeafe',
            label: after.label || 'After'
        });
        
        this.elements.push({
            type: 'label',
            x: centerX + 200 - boxWidth / 2,
            y: startY + boxHeight / 2 + 5,
            text: after.value.toString(),
            color: '#000000',
            fontSize: 18,
            align: 'center'
        });
        
        this.elements.push({
            type: 'label',
            x: centerX + 200 - boxWidth / 2,
            y: startY - 20,
            text: after.label || 'After',
            color: '#3b82f6',
            fontSize: 14,
            align: 'center'
        });
        
        this.saveState();
        this.render();
    }
    
    render() {
        // Clear canvas
        this.ctx.fillStyle = this.options.backgroundColor;
        this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);
        
        // Draw grid
        if (this.options.showGrid) {
            this.drawGrid();
        }
        
        // Draw all elements
        this.elements.forEach(el => this.drawElement(el));
        
        // Draw selection highlight
        if (this.selectedElement) {
            this.drawSelection(this.selectedElement);
        }
    }
    
    drawGrid() {
        this.ctx.strokeStyle = '#e5e7eb';
        this.ctx.lineWidth = 1;
        
        for (let x = 0; x <= this.canvas.width; x += this.options.gridSize) {
            this.ctx.beginPath();
            this.ctx.moveTo(x, 0);
            this.ctx.lineTo(x, this.canvas.height);
            this.ctx.stroke();
        }
        
        for (let y = 0; y <= this.canvas.height; y += this.options.gridSize) {
            this.ctx.beginPath();
            this.ctx.moveTo(0, y);
            this.ctx.lineTo(this.canvas.width, y);
            this.ctx.stroke();
        }
    }
    
    drawElement(el) {
        this.ctx.strokeStyle = el.color || this.currentColor;
        this.ctx.fillStyle = el.fillColor || this.currentFillColor;
        this.ctx.lineWidth = this.strokeWidth;
        
        if (el.type === 'bar') {
            this.ctx.fillRect(el.x, el.y, el.width, el.height);
            this.ctx.strokeRect(el.x, el.y, el.width, el.height);
        } else if (el.type === 'unit') {
            if (el.shape === 'circle') {
                this.ctx.beginPath();
                this.ctx.arc(el.x, el.y, el.size / 2, 0, Math.PI * 2);
                this.ctx.fill();
                this.ctx.stroke();
            } else if (el.shape === 'square') {
                this.ctx.fillRect(el.x - el.size / 2, el.y - el.size / 2, el.size, el.size);
                this.ctx.strokeRect(el.x - el.size / 2, el.y - el.size / 2, el.size, el.size);
            } else if (el.shape === 'triangle') {
                this.ctx.beginPath();
                this.ctx.moveTo(el.x, el.y - el.size / 2);
                this.ctx.lineTo(el.x + el.size / 2, el.y + el.size / 2);
                this.ctx.lineTo(el.x - el.size / 2, el.y + el.size / 2);
                this.ctx.closePath();
                this.ctx.fill();
                this.ctx.stroke();
            }
        } else if (el.type === 'label') {
            this.ctx.fillStyle = el.color || this.currentColor;
            this.ctx.font = `${el.fontSize || 14}px sans-serif`;
            this.ctx.textAlign = el.align || 'left';
            this.ctx.fillText(el.text, el.x, el.y);
        } else if (el.type === 'arrow') {
            this.drawArrow(el.x1, el.y1, el.x2, el.y2, el.color);
        } else if (el.type === 'bracket') {
            this.drawBracket(el.x1, el.y1, el.x2, el.y2, el.color);
        }
    }
    
    drawArrow(x1, y1, x2, y2, color) {
        const headLength = 10;
        const angle = Math.atan2(y2 - y1, x2 - x1);
        
        this.ctx.strokeStyle = color || this.currentColor;
        this.ctx.lineWidth = this.strokeWidth;
        
        this.ctx.beginPath();
        this.ctx.moveTo(x1, y1);
        this.ctx.lineTo(x2, y2);
        this.ctx.stroke();
        
        // Arrow head
        this.ctx.beginPath();
        this.ctx.moveTo(x2, y2);
        this.ctx.lineTo(x2 - headLength * Math.cos(angle - Math.PI / 6), y2 - headLength * Math.sin(angle - Math.PI / 6));
        this.ctx.lineTo(x2 - headLength * Math.cos(angle + Math.PI / 6), y2 - headLength * Math.sin(angle + Math.PI / 6));
        this.ctx.closePath();
        this.ctx.fillStyle = color || this.currentColor;
        this.ctx.fill();
    }
    
    drawBracket(x1, y1, x2, y2, color) {
        this.ctx.strokeStyle = color || this.currentColor;
        this.ctx.lineWidth = this.strokeWidth;
        
        const height = 20;
        
        this.ctx.beginPath();
        this.ctx.moveTo(x1, y1);
        this.ctx.lineTo(x1, y1 + height);
        this.ctx.lineTo(x2, y2 + height);
        this.ctx.lineTo(x2, y2);
        this.ctx.stroke();
    }
    
    drawSelection(el) {
        this.ctx.strokeStyle = '#3b82f6';
        this.ctx.lineWidth = 2;
        this.ctx.setLineDash([5, 5]);
        
        if (el.type === 'bar') {
            this.ctx.strokeRect(el.x - 2, el.y - 2, el.width + 4, el.height + 4);
        } else if (el.type === 'unit') {
            this.ctx.beginPath();
            this.ctx.arc(el.x, el.y, el.size / 2 + 5, 0, Math.PI * 2);
            this.ctx.stroke();
        } else if (el.type === 'label') {
            const metrics = this.ctx.measureText(el.text);
            this.ctx.strokeRect(el.x - 2, el.y - 14, metrics.width + 4, 18);
        }
        
        this.ctx.setLineDash([]);
    }
    
    drawTempElement() {
        if (!this.tempElement) return;
        
        this.ctx.globalAlpha = 0.5;
        this.drawElement(this.tempElement);
        this.ctx.globalAlpha = 1;
    }
    
    // Tool methods
    setTool(tool) {
        this.currentTool = tool;
        this.selectedElement = null;
        this.render();
    }
    
    setColor(color, fillColor) {
        this.currentColor = color;
        if (fillColor) this.currentFillColor = fillColor;
        
        if (this.selectedElement) {
            this.selectedElement.color = color;
            if (fillColor) this.selectedElement.fillColor = fillColor;
            this.saveState();
            this.render();
        }
    }
    
    // History methods
    saveState() {
        // Remove future history if we're not at the end
        if (this.historyIndex < this.history.length - 1) {
            this.history = this.history.slice(0, this.historyIndex + 1);
        }
        
        // Add new state
        this.history.push(JSON.parse(JSON.stringify(this.elements)));
        
        // Limit history size
        if (this.history.length > this.maxHistory) {
            this.history.shift();
        } else {
            this.historyIndex++;
        }
    }
    
    undo() {
        if (this.historyIndex > 0) {
            this.historyIndex--;
            this.elements = JSON.parse(JSON.stringify(this.history[this.historyIndex]));
            this.render();
        }
    }
    
    redo() {
        if (this.historyIndex < this.history.length - 1) {
            this.historyIndex++;
            this.elements = JSON.parse(JSON.stringify(this.history[this.historyIndex]));
            this.render();
        }
    }
    
    // Element manipulation
    deleteSelected() {
        if (this.selectedElement) {
            const index = this.elements.indexOf(this.selectedElement);
            if (index > -1) {
                this.elements.splice(index, 1);
                this.selectedElement = null;
                this.saveState();
                this.render();
            }
        }
    }
    
    clear() {
        this.elements = [];
        this.selectedElement = null;
        this.saveState();
        this.render();
    }
    
    // Export methods
    toPNG() {
        return this.canvas.toDataURL('image/png');
    }
    
    downloadPNG(filename = 'model.png') {
        const link = document.createElement('a');
        link.download = filename;
        link.href = this.toPNG();
        link.click();
    }
    
    toJSON() {
        return JSON.stringify({
            width: this.canvas.width,
            height: this.canvas.height,
            elements: this.elements
        });
    }
    
    fromJSON(json) {
        try {
            const data = JSON.parse(json);
            this.elements = data.elements || [];
            this.saveState();
            this.render();
            return true;
        } catch (e) {
            console.error('Failed to load model:', e);
            return false;
        }
    }
    
    // Getters for integration
    getElements() {
        return this.elements;
    }
    
    setElements(elements) {
        this.elements = elements;
        this.saveState();
        this.render();
    }
}

// Export for module systems
if (typeof module !== 'undefined' && module.exports) {
    module.exports = ModelCanvas;
}

# About Sean Foo

## What do you do?

I am a strategic operational leader and aspiring AI-native entrepreneur specializing in the commercialization of AI-driven solutions and digital transformation within the energy and fintech sectors.

## What businesses or projects are you working on?

- **Aurora Energy Research**: Serving as Head of BIO (Business Operations) for APAC, where I lead the regionalization of operations and build the infrastructure to support large-scale energy research and advisory.
- **Two Alpha Group**: Chief Business Officer leading a strategic transition toward an AI-driven quantitative trading platform and B2B partnership models.
- **Chainlink Community**: Enthusiast and volunteer host, focusing on building a technical community around decentralized AI and blockchain updates.
- **AI Advisory Beta**: Early adopter and tester of advanced AI-powered student advising tools to enhance educational outcomes.

## What's your professional background?

- **Aurora Energy Research** (Jan 08, 2024–Present): Regional Head of BIO for APAC, managing office expansion and operational excellence across Singapore, Australia, and India.
- **Stuart Wright Pte Ltd** (2008–2022): Advanced to Senior Manager, leading R&D teams to create the industry's first cloud-based barrier reporting software for the energy sector.
- **Technical Foundations**: Extensive experience in technical content strategy, quantitative investing, and drilling engineering (BP, Eaglewood Energy).
- **Education**: Executive MBA from Quantic School of Business and Technology and a Mechanical Engineering degree from the National University of Singapore.

## Who do you serve?

I serve APAC regional leadership, institutional energy clients, B2B financial partners, and a growing community of AI enthusiasts and retail investors seeking sophisticated, technology-led solutions.

## What tools do you use daily?

- **AI & Data**: Power BI, SQL, T-SQL, and generative AI tools (ChatGPT/GPT-4) for data modeling and operational analysis.
- **Operations**: SAP SuccessFactors, Navan, and ERP systems for billing and People & Culture management.
- **Productivity**: Microsoft Office Suite (heavy PowerPoint/Excel) and Google Workspace.

## Personal Mission: Education-Focused Schema

My work and personal development are guided by a unique focus on my two boys' education and learning (ages 11 and 6). I am particularly interested in preparing them for their future based on what we know today, and as time progresses.

**Core Goals:**
- Create learning apps, systems, and content that mirror the approach of **Squirrel AI**—using AI to identify and address individual learning gaps.
- Foster **critical thinking** and **leadership** skills through intentional design.
- Integrate **psychology** and **human communication** principles to make learning intuitive and effective.

**Ultimate Vision:**
Wrap everything I develop around **games**, so that my boys (and eventually other learners) learn without realizing it—transforming education into engaging, game‑based experiences that naturally build the skills they'll need for the future.

## Project ATOM‑SG Learnings (2026‑04‑08)

### Answer‑Key Pitfalls
- Letters vs numbers mismatch: Answer key may show "C" while question expects numeral
- Coding errors in answer keys: Some answers appear misaligned or wrong
- Need intelligent interpretation: Answer key should inform pedagogical intent, not be taken literally

### Pedagogical Pattern > Instance
- Capture **design parameters**, not specific answers (e.g., "count_range: within_20" not "answer: 19")
- Question is a **game design template**, not a data point
- Focus on skill type, visual arrangement, cognitive demand, answer format

### Schema Stability Across Levels
- Design core schema for Primary 1‑6 with extensible fields
- Earlier levels can have null values for advanced concepts
- Complexity scoring: Tier questions based on visual‑linguistic integration, multi‑skill dependency

### Game‑First Mindset
- Every extracted question must yield actionable game design hook
- Age‑specific adaptations: 6‑year‑old vs 11‑year‑old versions
- Complexity score drives level design and adaptive difficulty

### Cost Optimization
- Heuristics first (70‑80% of questions)
- Claude only for complex/ambiguous visuals (confidence < 0.7)
- Batch processing (8 images per API call) to minimize cost
- Estimated cost: ~$0.15‑$0.25 per 1000 questions vs $1.50‑$3.00

### Pipeline Improvements Needed
1. Smart answer‑key parsing with question‑type awareness
2. Visual‑number extraction from Claude descriptions
3. Question‑type classifier (counting vs MCQ vs writing)
4. Validation layer to flag mismatches
5. Complexity scoring based on graph structure
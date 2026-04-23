# Pilot Launch Checklist - ATOM-SG MVP

**Pilot Launch Target:** Week 2 (2026-04-26)  
**Current Date:** 2026-04-16  
**Days Remaining:** 10 days

---

## Countdown Timeline

### Day -11 (2026-04-15) - Verification Complete ✅
- [x] MVP Final Verification PASSED (23 tests, 22 passed, 0 failed)
- [x] Critical UX fixes implemented (14/14 issues)
- [x] All P0/P1 code fixes deployed
- [x] Backend stable and functional

### Day -10 (2026-04-16) - Deployment Artifacts Creation
- [x] Create Docker multi-stage build (Dockerfile)
- [x] Create Docker Compose configuration
- [x] Create system-aware install script (install.sh)
- [x] Create deployment documentation (DEPLOYMENT.md)
- [x] Create Nginx reverse proxy configuration
- [x] Create startup script (start.sh)
- [x] Create backup and restore scripts
- [x] Create health check script
- [ ] Test Docker build locally
- [ ] Test install script on clean environment

### Day -9 (2026-04-17) - Environment Preparation
- [ ] Set up pilot server (VPS/cloud instance)
- [ ] Configure firewall (ports 5000, 80, 443)
- [ ] Install Docker and Docker Compose on server
- [ ] Set up monitoring (logs, alerts)
- [ ] Configure DNS (if using domain)
- [ ] Set up SSL certificates (Let's Encrypt)
- [ ] Create deployment user with appropriate permissions

### Day -8 (2026-04-18) - First Deployment
- [ ] Deploy backend to pilot server
- [ ] Verify all services start correctly
- [ ] Run verification script on deployed instance
- [ ] Test all API endpoints
- [ ] Test OCR pipeline with sample scans
- [ ] Test rendering pipeline with sample problems
- [ ] Test frontend access and functionality
- [ ] Perform load test (simulate multiple users)

### Day -7 (2026-04-19) - Stakeholder Review
- [ ] Conduct hands-on review with educators
- [ ] Gather feedback on UX/UI improvements
- [ ] Adjust configuration based on feedback
- [ ] Update documentation based on feedback
- [ ] Create user guide for students/parents
- [ ] Create teacher/parent guide for monitoring progress

### Day -6 (2026-04-20) - Data Preparation
- [ ] Prepare baseline test problems (Week 1)
- [ ] Prepare practice problems (Weeks 2-4)
- [ ] Prepare transfer test problems (Week 5)
- [ ] Generate all required diagrams (renders)
- [ ] Verify diagram accuracy and proportions
- [ ] Create sample student accounts (if needed)
- [ ] Prepare sample data for demonstration

### Day -5 (2026-04-21) - Training & Documentation
- [ ] Create video walkthrough for students
- [ ] Create video walkthrough for parents/teachers
- [ ] Update FAQ based on common questions
- [ ] Prepare support contact information
- [ ] Set up support channel (email, chat, etc.)
- [ ] Train support team on common issues

### Day -4 (2026-04-22) - Final Testing
- [ ] End-to-end testing with real student persona
- [ ] Test baseline test PDF generation and printing
- [ ] Test scan upload and OCR processing
- [ ] Test daily practice flow (pathway radar + practice)
- [ ] Test triad feedback generation
- [ ] Test progress tracking and dashboard
- [ ] Test cross-thread collision detection
- [ ] Performance testing under load
- [ ] Security review (penetration testing if possible)

### Day -3 (2026-04-23) - Bug Fix & Polish
- [ ] Address any critical bugs found in testing
- [ ] Implement any last-minute UX improvements
- [ ] Update configuration for production
- [ ] Set up automated backups
- [ ] Set up log rotation
- [ ] Set up monitoring alerts
- [ ] Finalize all documentation

### Day -2 (2026-04-24) - Communication & Readiness
- [ ] Send pilot invitation to participants
- [ ] Distribute access instructions
- [ ] Schedule orientation session (if needed)
- [ ] Prepare contingency plan for technical issues
- [ ] Verify backup and restore procedures
- [ ] Conduct final health check
- [ ] Update status page (if applicable)

### Day -1 (2026-04-25) - Pre-Launch
- [ ] Final system check (all services healthy)
- [ ] Final backup before launch
- [ ] Monitor system resources (disk space, memory)
- [ ] Support team on standby
- [ ] Send reminder to participants
- [ ] Review launch checklist completion

### Day 0 (2026-04-26) - LAUNCH DAY
- [ ] Morning health check (6:00 AM)
- [ ] Verify all services running
- [ ] Monitor logs for errors
- [ ] Support team active
- [ ] Welcome first participants
- [ ] Monitor system performance
- [ ] Collect initial feedback

---

## Deployment Artifacts Status

### Created ✅
- [x] `Dockerfile` - Multi-stage build with Python 3.11, Tesseract, GL libraries
- [x] `docker-compose.yml` - Service definition with health checks
- [x] `install.sh` - System-aware installer for macOS/Ubuntu/RHEL/Arch
- [x] `DEPLOYMENT.md` - Comprehensive deployment guide
- [x] `nginx.conf` - Reverse proxy configuration
- [x] `start.sh` - Convenience startup script
- [x] Backup scripts (`backup.sh`, `restore_backup.sh`)
- [x] Health check script (`health_check.sh`)

### To Be Tested 🔄
- [ ] Docker build on clean environment
- [ ] Install script on different OS distributions
- [ ] Deployment on target server
- [ ] Backup and restore functionality

---

## Critical Success Criteria

### Technical Criteria
- [ ] Backend uptime > 99% during pilot
- [ ] API response time < 500ms (p95)
- [ ] OCR processing time < 30s per page
- [ ] Diagram rendering time < 10s
- [ ] No data loss incidents
- [ ] Successful daily backups

### Pedagogical Criteria
- [ ] ≥90% pathway identification accuracy on trained pathways
- [ ] ≥90% articulation Level 2+ rate on trained pathways
- [ ] ≥80% solving improvement from baseline on trained pathways
- [ ] ≥80% transfer accuracy on trained pathways (first 3 items)
- [ ] ≥90% daily practice completion rate

### User Experience Criteria
- [ ] Students can complete daily practice within 20 minutes
- [ ] Clear feedback on pathway identification errors
- [ ] Help available when stuck (I'm Stuck button)
- [ ] Progress visible on dashboard
- [ ] Mobile/tablet responsive design works

---

## Risk Assessment

### High Risk
| Risk | Mitigation |
|------|------------|
| **Server downtime during pilot** | Multiple availability zones, automatic failover, daily backups |
| **OCR accuracy below 70%** | Manual correction fallback, online practice mode alternative |
| **Student data loss** | Automated backups (hourly during pilot), test restore procedures |

### Medium Risk
| Risk | Mitigation |
|------|------------|
| **Slow performance under load** | Load testing before launch, auto-scaling configuration |
| **UX confusion for 11-year-olds** | Extensive testing with target age group, clear instructions |
| **Browser compatibility issues** | Test on Chrome, Safari, Edge; provide browser recommendations |

### Low Risk
| Risk | Mitigation |
|------|------------|
| **Diagram rendering errors** | Validation before display, fallback to simplified diagrams |
| **Network connectivity issues** | Offline mode for practice, local caching |

---

## Communication Plan

### Pre-Launch
- **Day -7:** Invitation email to participants
- **Day -3:** Reminder email with access instructions
- **Day -1:** Final reminder and schedule

### During Pilot
- **Daily:** Health status report (automated)
- **Weekly:** Progress summary email to parents/teachers
- **As needed:** Support responses within 4 hours

### Post-Pilot
- **Week 5:** Transfer test completion
- **Week 6:** Results analysis and report
- **Week 7:** Feedback collection and next steps

---

## Support Structure

### Tier 1: Self-Service
- FAQ documentation
- Video tutorials
- Troubleshooting guides

### Tier 2: Technical Support
- Email support (response within 4 hours)
- Chat support (during business hours)
- Common issue resolution scripts

### Tier 3: Escalation
- Developer on-call for critical issues
- Emergency patch deployment process
- Data recovery procedures

---

## Monitoring & Alerts

### System Monitoring
- **Uptime:** Pingdom or uptime robot
- **Performance:** New Relic or Datadog
- **Logs:** ELK stack or Papertrail
- **Backups:** Backup success/failure alerts

### Application Monitoring
- **API health:** `/api/v1/system/health`
- **Error rates:** >1% triggers alert
- **Response time:** >1s triggers alert
- **OCR success rate:** <70% triggers alert

### User Monitoring
- **Active users:** Daily active users count
- **Practice completion:** % of daily goals met
- **Error reports:** User-reported issues

---

## Budget & Resources

### Infrastructure Costs
- **Server:** $20-50/month (VPS with 2CPU, 4GB RAM)
- **Storage:** $10-20/month (SSD storage for artifacts)
- **Bandwidth:** $5-10/month (estimated)
- **Monitoring:** $0-50/month (depending on tools)

### Human Resources
- **Technical lead:** 2 hours/day during pilot
- **Support staff:** 1 hour/day during pilot
- **Educator oversight:** 1 hour/day during pilot

### Total Estimated Cost: $150-300 for 5-week pilot

---

## Success Metrics Tracking

### Daily Metrics (Automated Dashboard)
- Active users
- Practice sessions completed
- Average scores
- System uptime
- Error rates

### Weekly Metrics (Manual Review)
- Pathway identification accuracy trends
- Articulation level improvements
- Student engagement metrics
- User feedback summary

### Pilot Completion Metrics
- Baseline vs. transfer test improvement
- Student satisfaction survey results
- Teacher/parent feedback
- Technical performance report

---

## Contingency Plans

### Plan A: Minor Issues
- **Issue:** Single service failure
- **Response:** Automatic restart, alert to team
- **Resolution time:** <15 minutes

### Plan B: Major Issues
- **Issue:** Complete system failure
- **Response:** Failover to backup server, restore from latest backup
- **Resolution time:** <2 hours

### Plan C: Pedagogical Issues
- **Issue:** Students confused by interface
- **Response:** Emergency UX update, additional guidance materials
- **Resolution time:** <24 hours

### Plan D: Data Loss
- **Issue:** Corrupted or lost student data
- **Response:** Restore from backup, manual data entry if needed
- **Resolution time:** <4 hours

---

## Post-Pilot Evaluation

### Technical Evaluation
- System performance under load
- Bug frequency and severity
- Infrastructure cost efficiency
- Deployment process effectiveness

### Pedagogical Evaluation
- Student learning outcomes
- Teacher/parent satisfaction
- Engagement metrics analysis
- Improvement recommendations

### Business Evaluation
- Cost per student
- Scalability assessment
- Market fit validation
- Next phase planning

---

## Notes

- **Pilot Duration:** 5 weeks (2026-04-26 to 2026-05-30)
- **Participants:** Target 10-20 students (P6 level)
- **Success Definition:** 80% of participants show measurable improvement
- **Exit Criteria:** All success metrics met or exceeded

---

*Checklist last updated: 2026-04-16*  
*Next review: 2026-04-17*
# playpen

[![Hello World](https://github.com/e1054967/playpen/actions/workflows/hello-world.yml/badge.svg)](https://github.com/e1054967/playpen/actions/workflows/hello-world.yml)
[![Test & Quality](https://github.com/e1054967/playpen/actions/workflows/test-quality.yml/badge.svg)](https://github.com/e1054967/playpen/actions/workflows/test-quality.yml)
[![Maintenance](https://github.com/e1054967/playpen/actions/workflows/maintenance.yml/badge.svg)](https://github.com/e1054967/playpen/actions/workflows/maintenance.yml)

A comprehensive playground repository demonstrating GitHub Actions workflows, CI/CD patterns, and automation best practices.

## 🚀 Workflows

### Hello World
**File:** `.github/workflows/hello-world.yml`

A feature-rich workflow demonstrating:
- ✨ **Workflow dispatch inputs** - Customize OS selection, messages, and deployment
- 📊 **Matrix builds** - Runs on Ubuntu, macOS, and Windows
- ⚡ **Performance metrics** - Tracks execution time for each job
- 📦 **Artifacts** - Creates, uploads, and combines greetings from all platforms
- 🔒 **Attestation** - Signs artifacts with build provenance
- 💬 **PR comments** - Posts results to pull requests automatically
- 💾 **Caching** - Demonstrates cache usage patterns
- 🚀 **Deployment** - Manual approval gate with production environment
- ❌ **Failure notifications** - Alerts when workflows fail

**Triggers:**
- Push to main
- Pull requests
- Manual (with custom inputs)
- Schedule (weekly on Sundays)

### Release
**File:** `.github/workflows/release.yml`

Automated release workflow:
- 🏗️ **Multi-platform builds** - Creates artifacts for Linux, macOS, and Windows
- 📝 **Auto-generated release notes** - Includes changelog from commits
- 📦 **Asset uploads** - Attaches build artifacts to GitHub releases
- 💬 **Discussion creation** - Announces releases in GitHub Discussions
- 🎯 **Tag-triggered** - Runs automatically on version tags (`v*.*.*`)
- 🎛️ **Manual option** - Can also be triggered manually with custom tags

**Triggers:**
- Push tags (`v*.*.*`)
- Manual (with custom tag input)

### Test & Quality
**File:** `.github/workflows/test-quality.yml`

Comprehensive quality assurance:
- 🔍 **Linting** - Black, isort, flake8, pylint, yamllint
- 🧪 **Testing** - pytest across multiple Python versions and platforms
- 📊 **Coverage** - Generates and uploads coverage reports
-  **PR feedback** - Posts test results and coverage to pull requests

**Triggers:**
- Push to main
- Pull requests
- Manual
- Schedule (weekly on Mondays)

### Maintenance
**File:** `.github/workflows/maintenance.yml`

Automated repository maintenance:
- 🧹 **Artifact cleanup** - Removes old artifacts (configurable age)
- 💾 **Cache cleanup** - Clears unused caches to free storage
- 🌿 **Stale branch detection** - Reports branches with no recent activity
- 🔍 **Dependency audit** - Security checks for Python dependencies
- 🎛️ **Configurable** - Manual trigger with custom cleanup settings

**Triggers:**
- Schedule (weekly on Sundays at 3 AM UTC)
- Manual (with cleanup options)

## 🤖 Dependabot

**File:** `.github/dependabot.yml`

Automated dependency updates:
- 📦 **GitHub Actions** - Weekly updates for workflow actions
- 🐍 **Python packages** - Weekly updates for Python dependencies
- 🏷️ **Auto-labeling** - Tags PRs with appropriate labels
- 👥 **Auto-assignment** - Assigns updates to maintainers
- 📦 **Grouped updates** - Combines minor and patch updates

## 🎯 Features Demonstrated

### Workflow Patterns
- ✅ Matrix builds across multiple OS and versions
- ✅ Job dependencies and data flow
- ✅ Conditional job execution
- ✅ Manual approval gates with environments
- ✅ Reusable outputs between jobs
- ✅ Concurrency control
- ✅ Timeout management

### Artifacts & Caching
- ✅ Artifact creation and upload
- ✅ Multi-job artifact downloads
- ✅ Artifact attestation and signing
- ✅ Cache usage patterns
- ✅ Automated cleanup strategies

### GitHub Integration
- ✅ GitHub API via github-script
- ✅ PR comments and feedback
- ✅ Status checks and summaries
- ✅ Release automation
- ✅ Discussion creation

### Best Practices
- ✅ Minimal permissions (least privilege)
- ✅ Dependency management (Dependabot)
- ✅ Dependency security audit (pip-audit)
- ✅ Performance tracking
- ✅ Comprehensive logging
- ✅ Error handling and notifications
- ✅ Node.js 24 compatibility

## 🛠️ Usage

### Manual Workflow Triggers

All workflows support manual triggering with custom inputs:

1. Go to the **Actions** tab
2. Select a workflow from the left sidebar
3. Click **Run workflow** button
4. Configure inputs (if available)
5. Click **Run workflow** to start

### Creating a Release

```bash
# Tag a new version
git tag v1.0.0
git push origin v1.0.0

# The release workflow will automatically:
# - Build artifacts for all platforms
# - Create a GitHub release with notes
# - Upload build artifacts
# - Create a discussion announcement
```

### Environment Setup (for deployment)

To use the deployment job with manual approval:

1. Go to **Settings** → **Environments**
2. Create a new environment named `production`
3. Add required reviewers
4. Configure protection rules as needed

## 📚 Learning Resources

This repository demonstrates patterns from:
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Workflow syntax](https://docs.github.com/en/actions/reference/workflow-syntax-for-github-actions)
- [GitHub Script action](https://github.com/actions/github-script)
- [Dependabot](https://docs.github.com/en/code-security/dependabot)

## 📝 License

This is a playground repository for learning and experimentation.
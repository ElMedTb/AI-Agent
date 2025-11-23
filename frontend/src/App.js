import React, { useState } from 'react';
import axios from 'axios';
import './styles.css';

// Use relative URLs since frontend is served from the same Flask app
const API_BASE_URL = process.env.REACT_APP_API_URL || '';

function App() {
    const [formData, setFormData] = useState({
        employee_name: '',
        email: '',
        department: '',
        start_date: '',
        manager: '',
        position: ''
    });

    const [loading, setLoading] = useState(false);
    const [result, setResult] = useState(null);
    const [error, setError] = useState(null);

    const handleChange = (e) => {
        setFormData({
            ...formData,
            [e.target.name]: e.target.value
        });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        setLoading(true);
        setError(null);
        setResult(null);

        try {
            const response = await axios.post(`${API_BASE_URL}/api/onboard`, formData);
            setResult(response.data);
        } catch (err) {
            setError(err.response?.data?.message || 'An error occurred while starting the onboarding workflow');
        } finally {
            setLoading(false);
        }
    };

    const loadSampleData = async () => {
        try {
            const response = await axios.get(`${API_BASE_URL}/api/sample-data`);
            setFormData(response.data);
        } catch (err) {
            setError('Failed to load sample data');
        }
    };

    return (
        <div className="app">
            <header className="header">
                <div className="container">
                    <h1>🤖 HR Onboarding Assistant</h1>
                    <p className="subtitle">Powered by IBM watsonx Orchestrate</p>
                </div>
            </header>

            <main className="main">
                <div className="container">
                    <div className="card">
                        <h2>Start New Employee Onboarding</h2>
                        <p className="description">
                            Automate the onboarding process across email, calendar, Slack, documents, and task management.
                        </p>

                        <form onSubmit={handleSubmit} className="form">
                            <div className="form-group">
                                <label htmlFor="employee_name">Employee Name *</label>
                                <input
                                    type="text"
                                    id="employee_name"
                                    name="employee_name"
                                    value={formData.employee_name}
                                    onChange={handleChange}
                                    required
                                    placeholder="John Doe"
                                />
                            </div>

                            <div className="form-group">
                                <label htmlFor="email">Email Address *</label>
                                <input
                                    type="email"
                                    id="email"
                                    name="email"
                                    value={formData.email}
                                    onChange={handleChange}
                                    required
                                    placeholder="john.doe@company.com"
                                />
                            </div>

                            <div className="form-group">
                                <label htmlFor="department">Department *</label>
                                <select
                                    id="department"
                                    name="department"
                                    value={formData.department}
                                    onChange={handleChange}
                                    required
                                >
                                    <option value="">Select Department</option>
                                    <option value="Engineering">Engineering</option>
                                    <option value="Marketing">Marketing</option>
                                    <option value="Sales">Sales</option>
                                    <option value="HR">HR</option>
                                    <option value="Finance">Finance</option>
                                    <option value="Operations">Operations</option>
                                    <option value="Product">Product</option>
                                    <option value="Design">Design</option>
                                    <option value="Customer Success">Customer Success</option>
                                </select>
                            </div>

                            <div className="form-group">
                                <label htmlFor="position">Position</label>
                                <input
                                    type="text"
                                    id="position"
                                    name="position"
                                    value={formData.position}
                                    onChange={handleChange}
                                    placeholder="Software Engineer"
                                />
                            </div>

                            <div className="form-group">
                                <label htmlFor="start_date">Start Date *</label>
                                <input
                                    type="date"
                                    id="start_date"
                                    name="start_date"
                                    value={formData.start_date}
                                    onChange={handleChange}
                                    required
                                />
                            </div>

                            <div className="form-group">
                                <label htmlFor="manager">Manager</label>
                                <input
                                    type="text"
                                    id="manager"
                                    name="manager"
                                    value={formData.manager}
                                    onChange={handleChange}
                                    placeholder="Jane Smith"
                                />
                            </div>

                            <div className="form-actions">
                                <button type="button" onClick={loadSampleData} className="btn btn-secondary">
                                    Load Sample Data
                                </button>
                                <button type="submit" disabled={loading} className="btn btn-primary">
                                    {loading ? 'Starting Onboarding...' : 'Start Onboarding'}
                                </button>
                            </div>
                        </form>

                        {error && (
                            <div className="alert alert-error">
                                <strong>Error:</strong> {error}
                            </div>
                        )}

                        {result && (
                            <div className="result">
                                <div className={`alert alert-${result.status === 'success' ? 'success' : 'error'}`}>
                                    <h3>{result.status === 'success' ? '✅ Success!' : '❌ Error'}</h3>
                                    {result.summary && <p>{result.summary}</p>}

                                    {result.actions_completed && result.actions_completed.length > 0 && (
                                        <div className="actions-list">
                                            <h4>Actions Completed:</h4>
                                            <ul>
                                                {result.actions_completed.map((action, index) => (
                                                    <li key={index}>{action}</li>
                                                ))}
                                            </ul>
                                        </div>
                                    )}

                                    {result.workflow_id && (
                                        <p className="workflow-id">
                                            <small>Workflow ID: {result.workflow_id}</small>
                                        </p>
                                    )}
                                </div>
                            </div>
                        )}
                    </div>

                    <div className="info-card">
                        <h3>How It Works</h3>
                        <ol>
                            <li>Fill in the new employee details</li>
                            <li>Click "Start Onboarding" to trigger the workflow</li>
                            <li>IBM watsonx Orchestrate automatically:
                                <ul>
                                    <li>Sends welcome emails</li>
                                    <li>Creates calendar events</li>
                                    <li>Generates onboarding documents</li>
                                    <li>Posts Slack announcements</li>
                                    <li>Creates Jira tasks</li>
                                </ul>
                            </li>
                            <li>Get a summary of all completed actions</li>
                        </ol>
                    </div>
                </div>
            </main>

            <footer className="footer">
                <div className="container">
                    <p>Built with IBM watsonx Orchestrate | Hackathon Project</p>
                </div>
            </footer>
        </div>
    );
}

export default App;



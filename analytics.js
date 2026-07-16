/**
 * analytics.js
 * 
 * A utility script to automatically collect visitor data and send it 
 * to the Django Analytics Backend.
 * 
 * Usage in React:
 * 
 * import { sendVisitorAnalytics } from './analytics';
 * 
 * useEffect(() => {
 *   sendVisitorAnalytics('My Portfolio', 'http://127.0.0.1:8000/api/analytics/visit/');
 * }, []);
 */

export const sendVisitorAnalytics = async (websiteName, apiUrl) => {
    try {
        // Generate a simple session ID if not exists
        let sessionId = sessionStorage.getItem('analytics_session_id');
        if (!sessionId) {
            sessionId = crypto.randomUUID ? crypto.randomUUID() : Math.random().toString(36).substring(2, 15);
            sessionStorage.setItem('analytics_session_id', sessionId);
        }

        const payload = {
            website_name: websiteName,
            user_agent: navigator.userAgent,
            language: navigator.language || navigator.userLanguage,
            screen_resolution: `${window.screen.width}x${window.screen.height}`,
            timezone: Intl.DateTimeFormat().resolvedOptions().timeZone,
            referrer: document.referrer || null,
            current_page: window.location.pathname + window.location.search,
            session_id: sessionId,
            
            // Optional Geo Location (if you want to implement frontend geolocation)
            // country: null,
            // region: null,
            // city: null,
            // latitude: null,
            // longitude: null
        };

        const response = await fetch(apiUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(payload)
        });

        if (!response.ok) {
            console.error('Failed to send analytics:', await response.text());
        }
    } catch (error) {
        console.error('Error sending analytics:', error);
    }
};

"use client";

import { useState } from "react";

export default function Home() {
  const API_URL = "http://127.0.0.1:8000";

  const [url, setUrl] = useState("");
  const [loading, setLoading] = useState(false);
  const [dashboard, setDashboard] = useState<any>(null);

  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [chatLoading, setChatLoading] = useState(false);

  const [videoA, setVideoA] = useState("");
  const [videoB, setVideoB] = useState("");
  const [comparison, setComparison] = useState<any>(null);
  const [compareLoading, setCompareLoading] = useState(false);

  const [insights, setInsights] = useState("");
  const [insightsLoading, setInsightsLoading] = useState(false);

  const analyzeCreator = async () => {
    if (!url) {
      alert("Please enter a YouTube URL");
      return;
    }

    try {
      setLoading(true);

      const response = await fetch(
        `${API_URL}/creator-dashboard`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            youtube_url: url,
            instagram_url: "",
          }),
        }
      );

      const data = await response.json();
      setDashboard(data);
    } catch (error) {
      console.error(error);
      alert("Failed to connect to backend");
    } finally {
      setLoading(false);
    }
  };

  const askQuestion = async () => {
    if (!question) {
      alert("Please enter a question");
      return;
    }

    try {
      setChatLoading(true);

      const response = await fetch(
        `${API_URL}/chat`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            question,
          }),
        }
      );

      const data = await response.json();
      setAnswer(data.answer);
    } catch (error) {
      console.error(error);
      alert("Chat failed");
    } finally {
      setChatLoading(false);
    }
  };

  const compareVideos = async () => {
    try {
      setCompareLoading(true);

      const response = await fetch(
        `${API_URL}/compare-videos`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            video_a: videoA,
            video_b: videoB,
          }),
        }
      );

      const data = await response.json();
      setComparison(data);
    } catch (error) {
      console.error(error);
      alert("Comparison failed");
    } finally {
      setCompareLoading(false);
    }
  };

  const generateInsights = async () => {
    try {
      setInsightsLoading(true);

      const response = await fetch(
        `${API_URL}/video-insights`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            youtube_url: url,
            instagram_url: "",
          }),
        }
      );

      const data = await response.json();
      setInsights(data.insights);
    } catch (error) {
      console.error(error);
      alert("Insights failed");
    } finally {
      setInsightsLoading(false);
    }
  };

  return (
    <main className="min-h-screen bg-gray-100 p-8">
      <div className="max-w-5xl mx-auto">
        <h1 className="text-5xl font-bold text-center">
          CreatorIQ AI
        </h1>

        <p className="text-center text-gray-500 mt-3">
          AI Powered Creator Intelligence Platform
        </p>

        <div className="mt-10 bg-white p-6 rounded-xl shadow">
          <input
            type="text"
            placeholder="Paste YouTube URL"
            value={url}
            onChange={(e) => setUrl(e.target.value)}
            className="w-full border p-4 rounded-lg"
          />

          <button
            onClick={analyzeCreator}
            className="w-full bg-black text-white p-4 rounded-lg mt-4"
          >
            {loading ? "Analyzing..." : "Analyze Creator"}
          </button>
        </div>

        {dashboard && (
          <>
            <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mt-8">
              <div className="bg-white p-6 rounded-xl shadow">
                <h3 className="text-gray-500">Health Score</h3>
                <p className="text-4xl font-bold">
                  {dashboard.creator_health_score}
                </p>
              </div>

              <div className="bg-white p-6 rounded-xl shadow">
                <h3 className="text-gray-500">Growth Score</h3>
                <p className="text-4xl font-bold">
                  {dashboard.growth_audit?.growth_score}
                </p>
              </div>

              <div className="bg-white p-6 rounded-xl shadow">
                <h3 className="text-gray-500">Brand Score</h3>
                <p className="text-4xl font-bold">
                  {dashboard.brand_match?.creator_score}
                </p>
              </div>
            </div>

            <div className="mt-6 bg-white p-6 rounded-xl shadow">
              <h2 className="text-2xl font-bold">
                Dashboard Summary
              </h2>

              <p className="mt-3 text-gray-600">
                {dashboard.dashboard_summary}
              </p>
            </div>

            <div className="mt-6 bg-white p-6 rounded-xl shadow">
              <h2 className="text-2xl font-bold">
                Creator Analysis
              </h2>

              <p>
                <strong>Niche:</strong>{" "}
                {dashboard.creator_analysis?.analysis?.content_niche}
              </p>

              <p>
                <strong>Style:</strong>{" "}
                {dashboard.creator_analysis?.analysis?.creator_style}
              </p>

              <p>
                <strong>Audience:</strong>{" "}
                {dashboard.creator_analysis?.analysis?.target_audience}
              </p>
            </div>

            <div className="mt-6 bg-white p-6 rounded-xl shadow">
              <h2 className="text-2xl font-bold">
                Ask Creator Questions
              </h2>

              <input
                type="text"
                placeholder="What is this creator mainly talking about?"
                value={question}
                onChange={(e) => setQuestion(e.target.value)}
                className="w-full border p-4 rounded-lg mt-4"
              />

              <button
                onClick={askQuestion}
                className="w-full bg-blue-600 text-white p-4 rounded-lg mt-4"
              >
                {chatLoading ? "Thinking..." : "Ask AI"}
              </button>

              {answer && (
                <div className="mt-4 bg-gray-100 p-4 rounded-lg">
                  <p>{answer}</p>
                </div>
              )}
            </div>

            <div className="mt-6 bg-white p-6 rounded-xl shadow">
              <h2 className="text-2xl font-bold">
                Compare Videos
              </h2>

              <input
                type="text"
                placeholder="Video A URL"
                value={videoA}
                onChange={(e) => setVideoA(e.target.value)}
                className="w-full border p-4 rounded-lg mt-4"
              />

              <input
                type="text"
                placeholder="Video B URL"
                value={videoB}
                onChange={(e) => setVideoB(e.target.value)}
                className="w-full border p-4 rounded-lg mt-4"
              />

              <button
                onClick={compareVideos}
                className="w-full bg-green-600 text-white p-4 rounded-lg mt-4"
              >
                {compareLoading ? "Comparing..." : "Compare Videos"}
              </button>

              {comparison && (
                <div className="mt-4">
                  <p>
                    <strong>Video A Engagement:</strong>{" "}
                    {comparison.video_a?.engagement_rate}%
                  </p>

                  <p>
                    <strong>Video B Engagement:</strong>{" "}
                    {comparison.video_b?.engagement_rate}%
                  </p>

                  <pre className="whitespace-pre-wrap bg-gray-100 p-4 rounded-lg mt-4">
                    {comparison.comparison}
                  </pre>
                </div>
              )}
            </div>

            <div className="mt-6 bg-white p-6 rounded-xl shadow">
              <h2 className="text-2xl font-bold">
                AI Content Strategist
              </h2>

              <button
                onClick={generateInsights}
                className="w-full bg-purple-600 text-white p-4 rounded-lg mt-4"
              >
                {insightsLoading
                  ? "Generating..."
                  : "Generate Insights"}
              </button>

              {insights && (
                <pre className="whitespace-pre-wrap bg-gray-100 p-4 rounded-lg mt-4">
                  {insights}
                </pre>
              )}
            </div>
          </>
        )}
      </div>
    </main>
  );
}
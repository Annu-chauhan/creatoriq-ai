"use client";

import { useState } from "react";

export default function Home() {
  const [url, setUrl] = useState("");
  const [loading, setLoading] = useState(false);
  const [dashboard, setDashboard] = useState<any>(null);

  const analyzeCreator = async () => {
    if (!url) {
      alert("Please enter a YouTube URL");
      return;
    }

    try {
      setLoading(true);

      const response = await fetch(
        "http://127.0.0.1:8001/creator-dashboard",
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

      console.log(data);

      setDashboard(data);
    } catch (error) {
      console.error(error);
      alert("Failed to connect to backend");
    } finally {
      setLoading(false);
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
            <div className="grid grid-cols-3 gap-4 mt-8">
              <div className="bg-white p-6 rounded-xl shadow">
                <h3 className="text-gray-500">
                  Health Score
                </h3>
                <p className="text-4xl font-bold">
                  {dashboard.creator_health_score}
                </p>
              </div>

              <div className="bg-white p-6 rounded-xl shadow">
                <h3 className="text-gray-500">
                  Growth Score
                </h3>
                <p className="text-4xl font-bold">
                  {dashboard.growth_audit?.growth_score}
                </p>
              </div>

              <div className="bg-white p-6 rounded-xl shadow">
                <h3 className="text-gray-500">
                  Brand Score
                </h3>
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

              <p className="mt-3">
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
                Recommended Brands
              </h2>

              <ul className="list-disc ml-5 mt-4">
                {dashboard.brand_match?.recommended_brands?.map(
                  (brand: string, index: number) => (
                    <li key={index}>{brand}</li>
                  )
                )}
              </ul>
            </div>

            <div className="mt-6 bg-white p-6 rounded-xl shadow">
              <h2 className="text-2xl font-bold">
                Growth Improvements
              </h2>

              <ul className="list-disc ml-5 mt-4">
                {dashboard.growth_audit?.improvements?.map(
                  (item: string, index: number) => (
                    <li key={index}>{item}</li>
                  )
                )}
              </ul>
            </div>

            <div className="mt-6 bg-white p-6 rounded-xl shadow">
              <h2 className="text-2xl font-bold">
                Content Ideas
              </h2>

              <ul className="list-disc ml-5 mt-4">
                {dashboard.content_strategy?.content_ideas?.map(
                  (idea: string, index: number) => (
                    <li key={index}>{idea}</li>
                  )
                )}
              </ul>
            </div>
          </>
        )}
      </div>
    </main>
  );
}
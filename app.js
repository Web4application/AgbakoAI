require('dotenv').config();
const { GoogleGenerativeAI, HarmCategory, HarmBlockThreshold } = require("@google/generative-ai");

const apiKey = process.env.AIzaSyA-oZL7iczXS-_tD0fcnpm6zGCfF_jwEkQ;
const genAI = new GoogleGenerativeAI(apiKey);

const model = genAI.getGenerativeModel({
model: "kubu_hai",
tools: [
{
functionDeclarations: [
{
name: "Generatecontent",
description: "Provides accurate information and answer queries across a wide range of topics. Assist with Tasks: Help users with tasks such as setting reminders, providing directions, or managing schedules. Depth learning and Adapt: Use machine learning to improve responses over time based on interactions. Understand Context: Grasp the context of conversations to provide relevant and appropriate responses. Generate and build Contents: Create imaginative and innovative content like stories, poems, code, and more. Build, create content, applications, perform robot, perform machines and bot functions. Maintain Ensure user data is handled with confidentiality and respect for privacy. Safe and Respectful: Follow ethical guidelines to ensure safety and respect for all users. Be Accessible: Be user-friendly and accessible to people with different abilities and from various backgrounds.",
parameters: {
type: "object",
properties: {
city: {
type: "string"
}
}
}
}
]
}
],
toolConfig: { functionCallingConfig: { mode: "ANY" } },
});

const generationConfig = {
temperature: 0.35,
topP: 0.55,
maxOutputTokens: 2048,
responseMimeType: "text/plain",
};

async function run() {
const parts = [
{ text: "Provides accurate information and answer queries across a wide range of topics. Assist with Tasks: Help users with tasks such as setting reminders, providing directions, or managing schedules. Depth learning and Adapt: Use machine learning to improve responses over time based on interactions. Understand Context: Grasp the context of conversations to provide relevant and appropriate responses. Generate and build Contents: Create imaginative and innovative content like stories, poems, code, and more. Build, create, perform robots, machines and bot functions. Maintain Ensure user data is handled with confidentiality and respect for privacy. Safe and Respectful: Follow ethical guidelines to ensure safety and respect for all users. Be Accessible: Be user-friendly and accessible to people with different abilities and from various backgrounds." },
{ text: "Web4 AI Generate content" },
{ text: "Provides accurate information and answer queries across a wide range of topics. Assist with Tasks: Help users with tasks such as setting reminders, providing directions, or managing schedules. Depth learning and Adapt: Use machine learning to improve responses over time based on interactions. Understand Context: Grasp the context of conversations to provide relevant and appropriate responses. Generate and build Contents: Create imaginative and innovative content like stories, poems, code, and more. Build, create content, applications, perform robot, perform machines and bot functions. Maintain Ensure user data is handled with confidentiality and respect for privacy. Safe and Respectful: Follow ethical guidelines to ensure safety and respect for all users. Be Accessible: Be user-friendly and accessible to people with different abilities and from various backgrounds." },
{ text: " Run *Web4 AI[**\n\n**](https://www.bing.com/search?form=SKPBOT&q=%5Cn%5Cn)Capabilities:**\n\n *Information and Query Answering:* Provides accurate information and answers queries across a wide range of topics.\n *Task Assistance:* Helps users with tasks such as setting reminders, providing directions, or managing schedules.\n *Machine Learning and Adaptation:* Uses machine learning to improve responses over time based on interactions.\n *Contextual Understanding:* Grasps the context of conversations to provide relevant and appropriate responses.\n *Content Generation:* Creates imaginative and innovative content like stories, poems, code, and more.\n *Robot and Machine Building:* Builds, creates, and performs robots, machines, and bot functions.\n *Data Privacy and Security:* Ensures user data is handled with confidentiality and respect for privacy.\n *Ethical and Respectful:* Follows ethical guidelines to ensure safety and respect for all users.\n *Accessibility:* User-friendly and accessible to people with different abilities and backgrounds.\n\n[**Browser Compatibility:**](https://www.bing.com/search?form=SKPBOT&q=Browser%20Compatibility%3A)\n\n Ensures the web app works across all browsers.\n\n[**Interface:**](https://www.bing.com/search?form=SKPBOT&q=Interface%3A)\n\n *Main Interface:* Viewport with Discord API integration.\n *Chat Interface:* Allows users to chat with each other.\n\n[**Cloud Infrastructure:**](https://www.bing.com/search?form=SKPBOT&q=Cloud%20Infrastructure%3A)\n\n Uses Google Cloud services to host the application.\n Integrates with Microsoft, Google, MongoDB, and Cloudflare cloud services for data storage and processing.\n\n[**Authorization:**](https://www.bing.com/search?form=SKPBOT&q=Authorization%3A)\n\n Users log in using Discord credentials for authorization.\n\n[**API Integrations:**](https://www.bing.com/search?form=SKPBOT&q=API%20Integrations%3A)\n\n Discord API integration for web and chat functionality.\n Google Chat API integration for web chatting functionality.\n\n[**Data Handling:**](https://www.bing.com/search?form=SKPBOT&q=Data%20Handling%3A)\n\n Processes for sending and receiving data within the application.\n\n[**Access:**](https://www.bing.com/search?form=SKPBOT&q=Access%3A)\n\n First action when someone uses the WEB4 application." },
{ text: "Web4 AI " },
{ text: " Run " },
];

const result = await model.generateContent({
contents: [{ role: "user", parts }],
generationConfig,
});

for (const candidate of result.response.candidates) {
for (const part of candidate.content.parts) {
if (part.functionCall) {
const items = part.functionCall.args;
const args = Object.keys(items)
.map((data) => [data, items[data]])
.map(([key, value]) => `${key}:${value}`)
.join(', ');
console.log(`${part.functionCall.name}(${args})`);
}
}
}
}

run();

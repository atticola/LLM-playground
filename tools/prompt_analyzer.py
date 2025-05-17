#!/usr/bin/env python3
"""
Prompt Analyzer Tool

A simple tool to analyze prompts used with language models and provide insights
on their effectiveness based on best practices.
"""

import re
import sys
import argparse
from typing import Dict, List, Tuple
import os


class PromptAnalyzer:
    """Analyzes LLM prompts and provides feedback for improvement."""

    def __init__(self):
        self.best_practices = {
            "specificity": {
                "patterns": [
                    r"\bspecific\b",
                    r"\bdetail(ed)?\b",
                    r"\bexact(ly)?\b",
                    r"\bprecise(ly)?\b",
                ],
                "suggestions": [
                    "Consider adding more specific instructions",
                    "Include details about the expected format",
                    "Specify the level of detail you want in the response",
                ],
                "weight": 1.0,
            },
            "clarity": {
                "patterns": [
                    r"\bclear(ly)?\b",
                    r"\bexplain\b",
                    r"\bstep[s]? by step\b",
                    r"\bin order\b",
                ],
                "suggestions": [
                    "Break complex requests into steps",
                    "Use clear, direct language",
                    "Organize multi-part requests in a numbered list",
                ],
                "weight": 1.0,
            },
            "context": {
                "patterns": [
                    r"\bcontext\b",
                    r"\bbackground\b",
                    r"\bassume\b",
                    r"\bprevious(ly)?\b",
                ],
                "suggestions": [
                    "Provide relevant background information",
                    "Specify constraints or limitations",
                    "Mention any relevant assumptions",
                ],
                "weight": 0.8,
            },
            "examples": {
                "patterns": [
                    r"\bexample[s]?\b",
                    r"\blike this\b",
                    r"\bsuch as\b",
                    r"\bfor instance\b",
                ],
                "suggestions": [
                    "Include examples of desired output format",
                    "Show examples of the style or approach you want",
                    "Use few-shot examples for complex tasks",
                ],
                "weight": 0.7,
            },
            "role_prompting": {
                "patterns": [
                    r"\bact as\b",
                    r"\byou are\b",
                    r"\bassume the role\b",
                    r"\bbehave like\b",
                ],
                "suggestions": [
                    "Specify a relevant expert role for the LLM to assume",
                    "Define the character or expertise level for the response",
                    "Include details about the role's perspective",
                ],
                "weight": 0.6,
            },
            "format_specification": {
                "patterns": [
                    r"\bformat\b",
                    r"\bstructure\b",
                    r"\borganize\b",
                    r"\blayout\b",
                    r"\bsection[s]?\b",
                ],
                "suggestions": [
                    "Explicitly define the output format",
                    "Specify section headers or structure",
                    "Indicate if you want bullet points, paragraphs, etc.",
                ],
                "weight": 0.8,
            },
            "tone_specification": {
                "patterns": [
                    r"\btone\b",
                    r"\bstyle\b",
                    r"\bvoice\b",
                    r"\btechnical\b",
                    r"\bcasual\b",
                    r"\bformal\b",
                ],
                "suggestions": [
                    "Specify the desired tone (technical, casual, formal)",
                    "Indicate the level of technical language preferred",
                    "Define the writing style for the response",
                ],
                "weight": 0.5,
            },
            "constraints": {
                "patterns": [
                    r"\blimit\b",
                    r"\bno more than\b",
                    r"\bat most\b",
                    r"\bwithin\b",
                    r"\bconstraint[s]?\b",
                ],
                "suggestions": [
                    "Add length or scope constraints",
                    "Set clear boundaries for the response",
                    "Specify any limitations on the answer",
                ],
                "weight": 0.6,
            },
            "reasoning_request": {
                "patterns": [
                    r"\breason\b",
                    r"\brationalize\b",
                    r"\bexplain why\b",
                    r"\bjustify\b",
                    r"\bthink through\b",
                ],
                "suggestions": [
                    "Ask for step-by-step reasoning",
                    "Request explanation of the thought process",
                    "Use chain-of-thought prompting for complex problems",
                ],
                "weight": 0.8,
            },
            "audience_specification": {
                "patterns": [
                    r"\baudience\b",
                    r"\breader[s]?\b",
                    r"\bfor someone\b",
                    r"\bexplain to\b",
                ],
                "suggestions": [
                    "Specify the target audience (beginner, expert, etc.)",
                    "Indicate the assumed knowledge level of the reader",
                    "Define who will be reading the response",
                ],
                "weight": 0.5,
            },
        }

    def analyze_prompt(self, prompt: str) -> Dict:
        """
        Analyzes a prompt for adherence to best practices.
        
        Args:
            prompt: The prompt text to analyze
            
        Returns:
            Dict with analysis results
        """
        word_count = len(prompt.split())
        score_by_category = {}
        total_score = 0
        total_weight = 0
        
        # Check prompt against each best practice category
        for category, info in self.best_practices.items():
            category_score = 0
            for pattern in info["patterns"]:
                if re.search(pattern, prompt, re.IGNORECASE):
                    category_score = 1
                    break
            
            score_by_category[category] = {
                "score": category_score,
                "weight": info["weight"],
                "weighted_score": category_score * info["weight"],
                "suggestions": info["suggestions"] if category_score == 0 else []
            }
            
            total_score += category_score * info["weight"]
            total_weight += info["weight"]
        
        # Calculate overall score (0-100)
        overall_score = (total_score / total_weight) * 100 if total_weight > 0 else 0
        
        # Find missing best practices
        missing_practices = [
            {"category": cat, "suggestions": info["suggestions"]}
            for cat, info in score_by_category.items()
            if info["score"] == 0
        ]
        
        return {
            "word_count": word_count,
            "overall_score": round(overall_score, 1),
            "category_scores": score_by_category,
            "missing_practices": missing_practices,
            "strengths": [cat for cat, info in score_by_category.items() if info["score"] > 0],
            "prompt_length_assessment": self._assess_prompt_length(word_count)
        }
    
    def _assess_prompt_length(self, word_count: int) -> str:
        """Provides assessment of prompt length."""
        if word_count < 10:
            return "Very short - likely lacks sufficient detail"
        elif word_count < 30:
            return "Short - may need more specificity"
        elif word_count < 100:
            return "Moderate length - potentially good balance"
        elif word_count < 300:
            return "Long - good for complex tasks"
        else:
            return "Very long - consider splitting into multiple prompts"
    
    def suggest_improvements(self, analysis: Dict) -> List[str]:
        """
        Generates improvement suggestions based on analysis results.
        
        Args:
            analysis: Analysis results dictionary
            
        Returns:
            List of improvement suggestions
        """
        suggestions = []
        
        # Add length-based suggestions
        suggestions.append(f"Prompt length: {analysis['prompt_length_assessment']}")
        
        # Add suggestions for missing practices
        for practice in analysis['missing_practices']:
            category = practice['category'].replace('_', ' ').title()
            # Take just one suggestion per category to avoid overwhelming
            if practice['suggestions']:
                suggestions.append(f"{category}: {practice['suggestions'][0]}")
        
        # Add general suggestions based on score
        if analysis['overall_score'] < 50:
            suggestions.append("Overall: Your prompt would benefit from significant improvement in specificity and structure.")
        elif analysis['overall_score'] < 75:
            suggestions.append("Overall: Your prompt is good but could be enhanced with more clarity and context.")
        
        return suggestions

    def highlight_strengths(self, analysis: Dict) -> List[str]:
        """Highlights the strengths of the prompt."""
        if not analysis['strengths']:
            return ["No specific strengths detected."]
        
        strengths = []
        for strength in analysis['strengths']:
            formatted_strength = strength.replace('_', ' ').title()
            strengths.append(f"✓ {formatted_strength}")
        
        return strengths


def format_output(analysis: Dict) -> str:
    """Format analysis results into readable output."""
    analyzer = PromptAnalyzer()
    
    output = []
    output.append(f"==== Prompt Analysis ====")
    output.append(f"Overall Score: {analysis['overall_score']}/100")
    output.append(f"Word Count: {analysis['word_count']} words")
    output.append(f"Length Assessment: {analysis['prompt_length_assessment']}")
    output.append("\n== Strengths ==")
    
    strengths = analyzer.highlight_strengths(analysis)
    output.extend(strengths)
    
    output.append("\n== Suggested Improvements ==")
    suggestions = analyzer.suggest_improvements(analysis)
    for suggestion in suggestions:
        if not suggestion.startswith("Prompt length:"):  # Already showed this
            output.append(f"• {suggestion}")
    
    output.append("\n== Category Scores ==")
    for category, info in analysis['category_scores'].items():
        formatted_category = category.replace('_', ' ').title()
        output.append(f"{formatted_category}: {info['score']} (Weight: {info['weight']})")
    
    return "\n".join(output)


def main():
    parser = argparse.ArgumentParser(description="Analyze LLM prompts and suggest improvements.")
    parser.add_argument("prompt_file", nargs="?", type=str, help="File containing the prompt to analyze")
    parser.add_argument("--prompt", "-p", type=str, help="Prompt text to analyze directly")
    parser.add_argument("--output", "-o", type=str, help="Output file for analysis results")
    
    args = parser.parse_args()
    
    # Get prompt text from file or direct input
    prompt_text = ""
    if args.prompt:
        prompt_text = args.prompt
    elif args.prompt_file:
        try:
            with open(args.prompt_file, 'r') as file:
                prompt_text = file.read()
        except FileNotFoundError:
            print(f"Error: File not found: {args.prompt_file}")
            sys.exit(1)
    else:
        print("Please provide a prompt using --prompt or specify a prompt file.")
        sys.exit(1)
    
    # Analyze the prompt
    analyzer = PromptAnalyzer()
    analysis = analyzer.analyze_prompt(prompt_text)
    
    # Format and output results
    output_text = format_output(analysis)
    
    if args.output:
        with open(args.output, 'w') as file:
            file.write(output_text)
        print(f"Analysis saved to {args.output}")
    else:
        print(output_text)


if __name__ == "__main__":
    main() 
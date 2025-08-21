"""
LLM Service for AI integration with OpenAI and Claude.
"""

from typing import Optional, Dict, Any, List
import openai
import anthropic
from app.core.config import settings
import logging

logger = logging.getLogger(__name__)

class LLMService:
    """Service for interacting with Large Language Models."""
    
    def __init__(self):
        self.openai_client = None
        self.anthropic_client = None
        
        if settings.OPENAI_API_KEY:
            self.openai_client = openai.OpenAI(api_key=settings.OPENAI_API_KEY)
        
        if settings.ANTHROPIC_API_KEY:
            self.anthropic_client = anthropic.Anthropic(api_key=settings.ANTHROPIC_API_KEY)
    
    async def generate_with_openai(
        self,
        prompt: str,
        model: str = "gpt-4",
        temperature: float = 0.7,
        max_tokens: int = 1000,
        **kwargs
    ) -> Optional[str]:
        """Generate text using OpenAI models."""
        if not self.openai_client:
            logger.warning("OpenAI client not configured")
            return None
        
        try:
            response = await self.openai_client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                temperature=temperature,
                max_tokens=max_tokens,
                **kwargs
            )
            return response.choices[0].message.content
        except Exception as e:
            logger.error(f"OpenAI API error: {e}")
            return None
    
    async def generate_with_claude(
        self,
        prompt: str,
        model: str = "claude-3-sonnet-20240229",
        temperature: float = 0.7,
        max_tokens: int = 1000,
        **kwargs
    ) -> Optional[str]:
        """Generate text using Claude models."""
        if not self.anthropic_client:
            logger.warning("Anthropic client not configured")
            return None
        
        try:
            response = await self.anthropic_client.messages.create(
                model=model,
                max_tokens=max_tokens,
                temperature=temperature,
                messages=[{"role": "user", "content": prompt}],
                **kwargs
            )
            return response.content[0].text
        except Exception as e:
            logger.error(f"Claude API error: {e}")
            return None
    
    async def generate_project_plan(
        self,
        project_description: str,
        constraints: List[str] = None,
        model: str = "gpt-4"
    ) -> Dict[str, Any]:
        """Generate a project plan using AI."""
        prompt = f"""
        Create a detailed project plan for the following project:
        
        Project Description: {project_description}
        
        Constraints: {', '.join(constraints) if constraints else 'None'}
        
        Please provide:
        1. Project timeline with phases
        2. Key tasks and milestones
        3. Resource requirements
        4. Risk assessment
        5. Success metrics
        
        Format the response as a structured plan.
        """
        
        response = await self.generate_with_openai(prompt, model=model)
        
        if response:
            return {
                "plan": response,
                "model": model,
                "status": "success"
            }
        else:
            return {
                "plan": "Unable to generate plan",
                "model": model,
                "status": "error"
            }
    
    async def analyze_project_health(
        self,
        project_data: Dict[str, Any],
        model: str = "claude-3-sonnet-20240229"
    ) -> Dict[str, Any]:
        """Analyze project health and provide recommendations."""
        prompt = f"""
        Analyze the following project data and provide health assessment:
        
        Project Data: {project_data}
        
        Please provide:
        1. Health score (0-100)
        2. Key risks and issues
        3. Recommendations for improvement
        4. Timeline impact assessment
        
        Format as a structured analysis.
        """
        
        response = await self.generate_with_claude(prompt, model=model)
        
        if response:
            return {
                "analysis": response,
                "model": model,
                "status": "success"
            }
        else:
            return {
                "analysis": "Unable to analyze project",
                "model": model,
                "status": "error"
            }
    
    async def generate_standup_summary(
        self,
        updates: List[Dict[str, Any]],
        model: str = "gpt-4"
    ) -> Dict[str, Any]:
        """Generate standup summary from team updates."""
        updates_text = "\n".join([
            f"- {update.get('name', 'Unknown')}: {update.get('update', 'No update')}"
            for update in updates
        ])
        
        prompt = f"""
        Generate a concise standup summary from the following team updates:
        
        {updates_text}
        
        Please provide:
        1. Key accomplishments
        2. Current blockers
        3. Next steps
        4. Team morale assessment
        
        Format as a structured summary.
        """
        
        response = await self.generate_with_openai(prompt, model=model)
        
        if response:
            return {
                "summary": response,
                "model": model,
                "status": "success"
            }
        else:
            return {
                "summary": "Unable to generate summary",
                "model": model,
                "status": "error"
            }

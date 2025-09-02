package com.ayush.user;
 
import org.springframework.web.bind.annotation.*;
 
@RestController
@RequestMapping("/claude")
@CrossOrigin(origins = "*")
public class ClaudeController {
 
    private final ClaudeService claudeService;
 
    public ClaudeController(ClaudeService claudeService) {
        this.claudeService = claudeService;
    }
 
    @GetMapping("/ask")
    public String ask(@RequestParam String q) {
        return claudeService.askClaude(q);
    }

    @GetMapping("/health")
    public String healthCheck() {
        return "working";
    }
}

﻿using Microsoft.AspNetCore.Mvc;
using SteamBot.Services;

namespace SteamBot.Controllers
{
    [Route("api/bot")]
    [ApiController]
    public class BotController : ControllerBase
    {
        [HttpPost("/sendsingle")]
        public ActionResult<string> SendOne(string userId, string messageText)
        {
            var service = new MessageService(messageText);
            var isSent = service.SendSingle(userId);
            return Ok(isSent);
        }

        [HttpPost("/sendall")]
        public IActionResult SendAll(string messageText)
        {
            var service = new MessageService(messageText);
            var isSent = service.SendAllFriends();
            return Ok(isSent);
        }

        [HttpPost("/acceptFriendsAndSendMessage")]
        public IActionResult AcceptFriendsRequestsAndSendMessage(string messageText)
        {
            var service = new MessageService(messageText);
            var isSent = service.AcceptFriendsAndSendMessage();
            return Ok(isSent); // If false, no pending friends requests.
        }
    }
}
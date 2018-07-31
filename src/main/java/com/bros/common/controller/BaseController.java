package com.bros.common.controller;

import com.bros.system.domain.UserToken;
import org.springframework.stereotype.Controller;
import com.bros.common.utils.ShiroUtils;
import com.bros.system.domain.UserDO;

@Controller
public class BaseController {
	public UserDO getUser() {
		return ShiroUtils.getUser();
	}

	public Long getUserId() {
		return getUser().getUserId();
	}

	public String getUsername() {
		return getUser().getUsername();
	}
}
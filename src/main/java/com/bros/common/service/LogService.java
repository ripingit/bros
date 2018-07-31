package com.bros.common.service;

import java.util.List;

import org.springframework.stereotype.Service;

import com.bros.common.domain.LogDO;
import com.bros.common.domain.PageDO;
import com.bros.common.utils.Query;
@Service
public interface LogService {
	void save(LogDO logDO);
	PageDO<LogDO> queryList(Query query);
	int remove(Long id);
	int batchRemove(Long[] ids);
}

package org.sparqloversms.algorithm.procedures.models;

import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.serializer.PropertyFilter;

public abstract class ProcedureReport {

    public String toJSON() {
        PropertyFilter filter = (source, name, value) -> !"output".equals(name);
        return JSON.toJSONString(this, filter);
    }

    public abstract String getOutput();
}

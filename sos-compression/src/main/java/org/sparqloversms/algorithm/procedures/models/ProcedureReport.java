package org.sparqloversms.algorithm.procedures.models;

import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.serializer.PropertyFilter;

public abstract class ProcedureReport {

    public String toJSON() {
        PropertyFilter filter = new PropertyFilter() {
            @Override
            public boolean apply(Object source, String name, Object value) {
                return !"output".equals(name);
            }
        };

        return JSON.toJSONString(this, filter);
    }

    public abstract String getOutput();
}

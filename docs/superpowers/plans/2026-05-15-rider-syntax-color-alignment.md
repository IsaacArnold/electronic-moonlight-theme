# Rider Syntax Color Alignment Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Align Rider/JetBrains color scheme attributes with the VS Code theme's effective syntax highlighting colors — fixing mismatched values and adding missing JS/TS language-specific attribute blocks.

**Architecture:** Pure XML edits to three color scheme files. The standalone `.icls` is edited first, then copied to the plugin `colors/` copy. The `colorSchemes/` XML uses the same attributes but omits `#` prefixes on hex values, so it is edited separately with the same logical changes. No new files are created.

**Tech Stack:** JetBrains color scheme XML (`.icls` and `.xml`), git

---

### Task 1: Create feature branch

**Files:** none

- [ ] **Step 1: Create and switch to branch**

```bash
git checkout -b feature/rider-syntax-color-alignment
```

Expected: `Switched to a new branch 'feature/rider-syntax-color-alignment'`

---

### Task 2: Fix Part 1 color mismatches in `jetbrains/Electronic Moonlight.icls`

**Files:**
- Modify: `jetbrains/Electronic Moonlight.icls`

- [ ] **Step 1: Fix `LOCAL_VARIABLE`**

Find and replace:
```xml
    <option name="LOCAL_VARIABLE">
      <value>
        <option name="FOREGROUND" value="#C8D3F5" />
      </value>
    </option>
```
With:
```xml
    <option name="LOCAL_VARIABLE">
      <value>
        <option name="FOREGROUND" value="#E26674" />
      </value>
    </option>
```

- [ ] **Step 2: Fix `REASSIGNED_LOCAL_VARIABLE_ATTRIBUTES`**

Find and replace:
```xml
    <option name="REASSIGNED_LOCAL_VARIABLE_ATTRIBUTES">
      <value>
        <option name="FOREGROUND" value="#C8D3F5" />
      </value>
    </option>
```
With:
```xml
    <option name="REASSIGNED_LOCAL_VARIABLE_ATTRIBUTES">
      <value>
        <option name="FOREGROUND" value="#E26674" />
      </value>
    </option>
```

- [ ] **Step 3: Fix `FUNCTION_CALL`**

Find and replace:
```xml
    <option name="FUNCTION_CALL">
      <value>
        <option name="FOREGROUND" value="#82AAFF" />
      </value>
    </option>
```
With:
```xml
    <option name="FUNCTION_CALL">
      <value>
        <option name="FOREGROUND" value="#65BCFF" />
      </value>
    </option>
```

- [ ] **Step 4: Fix `CONSTANT`**

Find and replace:
```xml
    <option name="CONSTANT">
      <value>
        <option name="FOREGROUND" value="#FF98A4" />
      </value>
    </option>
```
With:
```xml
    <option name="CONSTANT">
      <value>
        <option name="FOREGROUND" value="#E76572" />
      </value>
    </option>
```

- [ ] **Step 5: Fix `ENUM_CONST_ATTRIBUTES`**

Find and replace:
```xml
    <option name="ENUM_CONST_ATTRIBUTES">
      <value>
        <option name="FOREGROUND" value="#FF98A4" />
      </value>
    </option>
```
With:
```xml
    <option name="ENUM_CONST_ATTRIBUTES">
      <value>
        <option name="FOREGROUND" value="#E76572" />
      </value>
    </option>
```

- [ ] **Step 6: Fix `HTML_ATTRIBUTE_VALUE`**

Find and replace:
```xml
    <option name="HTML_ATTRIBUTE_VALUE">
      <value>
        <option name="FOREGROUND" value="#C3E88D" />
      </value>
    </option>
```
With:
```xml
    <option name="HTML_ATTRIBUTE_VALUE">
      <value>
        <option name="FOREGROUND" value="#56A3B1" />
      </value>
    </option>
```

- [ ] **Step 7: Fix `XML_ATTRIBUTE_VALUE`**

Find and replace:
```xml
    <option name="XML_ATTRIBUTE_VALUE">
      <value>
        <option name="FOREGROUND" value="#C3E88D" />
      </value>
    </option>
```
With:
```xml
    <option name="XML_ATTRIBUTE_VALUE">
      <value>
        <option name="FOREGROUND" value="#56A3B1" />
      </value>
    </option>
```

- [ ] **Step 8: Fix `ReSharper.ReSharperLOCAL_VARIABLE_IDENTIFIER`**

Find and replace:
```xml
    <option name="ReSharper.ReSharperLOCAL_VARIABLE_IDENTIFIER">
      <value>
        <option name="FOREGROUND" value="#C8D3F5" />
      </value>
    </option>
```
With:
```xml
    <option name="ReSharper.ReSharperLOCAL_VARIABLE_IDENTIFIER">
      <value>
        <option name="FOREGROUND" value="#E26674" />
      </value>
    </option>
```

- [ ] **Step 9: Fix `ReSharper.ReSharperMUTABLE_LOCAL_VARIABLE_IDENTIFIER`**

Find and replace:
```xml
    <option name="ReSharper.ReSharperMUTABLE_LOCAL_VARIABLE_IDENTIFIER">
      <value>
        <option name="FOREGROUND" value="#C8D3F5" />
      </value>
    </option>
```
With:
```xml
    <option name="ReSharper.ReSharperMUTABLE_LOCAL_VARIABLE_IDENTIFIER">
      <value>
        <option name="FOREGROUND" value="#E26674" />
      </value>
    </option>
```

- [ ] **Step 10: Fix `ReSharper.ReSharperCAPTURED_VARIABLE_IDENTIFIER`**

Find and replace:
```xml
    <option name="ReSharper.ReSharperCAPTURED_VARIABLE_IDENTIFIER">
      <value>
        <option name="FOREGROUND" value="#C8D3F5" />
      </value>
    </option>
```
With:
```xml
    <option name="ReSharper.ReSharperCAPTURED_VARIABLE_IDENTIFIER">
      <value>
        <option name="FOREGROUND" value="#E26674" />
      </value>
    </option>
```

- [ ] **Step 11: Verify all Part 1 changes**

```bash
grep -E "E26674|65BCFF|E76572|56A3B1" "jetbrains/Electronic Moonlight.icls"
```

Expected: lines containing the new values — `E26674` should appear 5 times (LOCAL_VARIABLE, REASSIGNED_LOCAL_VARIABLE_ATTRIBUTES, and the 3 ReSharper variants), `65BCFF` once, `E76572` twice, `56A3B1` twice.

---

### Task 3: Add Part 2 new attribute blocks to `jetbrains/Electronic Moonlight.icls`

**Files:**
- Modify: `jetbrains/Electronic Moonlight.icls`

- [ ] **Step 1: Add `CSS_UNIT` to the CSS / SCSS section**

Locate the `CSS_VARIABLE` block (currently the last item in the `<!-- CSS / SCSS -->` section). Insert `CSS_UNIT` immediately after it:

```xml
    <option name="CSS_UNIT">
      <value>
        <option name="FOREGROUND" value="#D59DF6" />
      </value>
    </option>
```

- [ ] **Step 2: Add the JavaScript / TypeScript section**

Insert the following block immediately after the `CSS_UNIT` entry you just added (before the `<!-- Markdown -->` comment):

```xml
    <!-- JavaScript / TypeScript -->
    <option name="JAVA_SCRIPT_LOCAL_VARIABLE">
      <value>
        <option name="FOREGROUND" value="#E26674" />
      </value>
    </option>
    <option name="JAVA_SCRIPT_GLOBAL_VARIABLE">
      <value>
        <option name="FOREGROUND" value="#FFC777" />
      </value>
    </option>
    <option name="JAVA_SCRIPT_PARAMETER">
      <value>
        <option name="FOREGROUND" value="#FCA7EA" />
      </value>
    </option>
    <option name="JAVA_SCRIPT_INSTANCE_MEMBER_VARIABLE">
      <value>
        <option name="FOREGROUND" value="#A9B8E8" />
      </value>
    </option>
    <option name="JAVA_SCRIPT_STATIC_MEMBER_VARIABLE">
      <value>
        <option name="FOREGROUND" value="#FF966C" />
      </value>
    </option>
    <option name="JAVA_SCRIPT_FUNCTION_DECLARATION">
      <value>
        <option name="FOREGROUND" value="#82AAFF" />
      </value>
    </option>
    <option name="JAVA_SCRIPT_INSTANCE_MEMBER_FUNCTION">
      <value>
        <option name="FOREGROUND" value="#82AAFF" />
      </value>
    </option>
    <option name="JAVA_SCRIPT_STATIC_MEMBER_FUNCTION">
      <value>
        <option name="FOREGROUND" value="#82AAFF" />
      </value>
    </option>
    <option name="JAVA_SCRIPT_KEYWORD">
      <value>
        <option name="FOREGROUND" value="#C099FF" />
        <option name="FONT_TYPE" value="2" />
      </value>
    </option>
    <option name="JAVA_SCRIPT_REGEXP">
      <value>
        <option name="FOREGROUND" value="#B4F9F8" />
      </value>
    </option>
    <option name="JAVA_SCRIPT_VALID_STRING_ESCAPE">
      <value>
        <option name="FOREGROUND" value="#86E1FC" />
      </value>
    </option>
    <option name="JAVA_SCRIPT_TEMPLATE_LITERAL">
      <value>
        <option name="FOREGROUND" value="#86E1FC" />
      </value>
    </option>
    <option name="JAVA_SCRIPT_MODULE_NAME">
      <value>
        <option name="FOREGROUND" value="#C3E88D" />
      </value>
    </option>
```

- [ ] **Step 3: Verify new attributes present**

```bash
grep -c "JAVA_SCRIPT_" "jetbrains/Electronic Moonlight.icls"
```

Expected: `13`

```bash
grep "CSS_UNIT" "jetbrains/Electronic Moonlight.icls"
```

Expected: one line containing `CSS_UNIT`

- [ ] **Step 4: Validate XML is well-formed**

```bash
xmllint --noout "jetbrains/Electronic Moonlight.icls" && echo "XML valid"
```

Expected: `XML valid`

If `xmllint` is unavailable: `brew install libxml2`

- [ ] **Step 5: Commit**

```bash
git add "jetbrains/Electronic Moonlight.icls"
git commit -m "feat: align standalone Rider color scheme with VS Code syntax highlighting"
```

---

### Task 4: Sync changes to `jetbrains-plugin/src/main/resources/colors/Electronic Moonlight.icls`

**Files:**
- Modify: `jetbrains-plugin/src/main/resources/colors/Electronic Moonlight.icls`

This file is a copy of the standalone `.icls`. Apply every change from Tasks 2–3 identically (same format, same `#` prefix on hex values).

- [ ] **Step 1: Copy the updated standalone file over the plugin copy**

```bash
cp "jetbrains/Electronic Moonlight.icls" "jetbrains-plugin/src/main/resources/colors/Electronic Moonlight.icls"
```

- [ ] **Step 2: Confirm the files are now identical**

```bash
diff "jetbrains/Electronic Moonlight.icls" "jetbrains-plugin/src/main/resources/colors/Electronic Moonlight.icls"
```

Expected: no output (files are identical)

- [ ] **Step 3: Validate XML**

```bash
xmllint --noout "jetbrains-plugin/src/main/resources/colors/Electronic Moonlight.icls" && echo "XML valid"
```

Expected: `XML valid`

- [ ] **Step 4: Commit**

```bash
git add "jetbrains-plugin/src/main/resources/colors/Electronic Moonlight.icls"
git commit -m "feat: sync plugin colors icls with standalone"
```

---

### Task 5: Fix Part 1 color mismatches in `jetbrains-plugin/src/main/resources/colorSchemes/Electronic Moonlight.xml`

**Files:**
- Modify: `jetbrains-plugin/src/main/resources/colorSchemes/Electronic Moonlight.xml`

This file uses the same attribute names but **omits `#` on hex values** (e.g. `value="C8D3F5"` not `value="#C8D3F5"`).

- [ ] **Step 1: Fix `LOCAL_VARIABLE`**

Find and replace:
```xml
    <option name="LOCAL_VARIABLE">
      <value>
        <option name="FOREGROUND" value="C8D3F5" />
      </value>
    </option>
```
With:
```xml
    <option name="LOCAL_VARIABLE">
      <value>
        <option name="FOREGROUND" value="E26674" />
      </value>
    </option>
```

- [ ] **Step 2: Fix `REASSIGNED_LOCAL_VARIABLE_ATTRIBUTES`**

Find and replace:
```xml
    <option name="REASSIGNED_LOCAL_VARIABLE_ATTRIBUTES">
      <value>
        <option name="FOREGROUND" value="C8D3F5" />
      </value>
    </option>
```
With:
```xml
    <option name="REASSIGNED_LOCAL_VARIABLE_ATTRIBUTES">
      <value>
        <option name="FOREGROUND" value="E26674" />
      </value>
    </option>
```

- [ ] **Step 3: Fix `FUNCTION_CALL`**

Find and replace:
```xml
    <option name="FUNCTION_CALL">
      <value>
        <option name="FOREGROUND" value="82AAFF" />
      </value>
    </option>
```
With:
```xml
    <option name="FUNCTION_CALL">
      <value>
        <option name="FOREGROUND" value="65BCFF" />
      </value>
    </option>
```

- [ ] **Step 4: Fix `CONSTANT`**

Find and replace:
```xml
    <option name="CONSTANT">
      <value>
        <option name="FOREGROUND" value="FF98A4" />
      </value>
    </option>
```
With:
```xml
    <option name="CONSTANT">
      <value>
        <option name="FOREGROUND" value="E76572" />
      </value>
    </option>
```

- [ ] **Step 5: Fix `ENUM_CONST_ATTRIBUTES`**

Find and replace:
```xml
    <option name="ENUM_CONST_ATTRIBUTES">
      <value>
        <option name="FOREGROUND" value="FF98A4" />
      </value>
    </option>
```
With:
```xml
    <option name="ENUM_CONST_ATTRIBUTES">
      <value>
        <option name="FOREGROUND" value="E76572" />
      </value>
    </option>
```

- [ ] **Step 6: Fix `HTML_ATTRIBUTE_VALUE`**

Find and replace:
```xml
    <option name="HTML_ATTRIBUTE_VALUE">
      <value>
        <option name="FOREGROUND" value="C3E88D" />
      </value>
    </option>
```
With:
```xml
    <option name="HTML_ATTRIBUTE_VALUE">
      <value>
        <option name="FOREGROUND" value="56A3B1" />
      </value>
    </option>
```

- [ ] **Step 7: Fix `XML_ATTRIBUTE_VALUE`**

Find and replace:
```xml
    <option name="XML_ATTRIBUTE_VALUE">
      <value>
        <option name="FOREGROUND" value="C3E88D" />
      </value>
    </option>
```
With:
```xml
    <option name="XML_ATTRIBUTE_VALUE">
      <value>
        <option name="FOREGROUND" value="56A3B1" />
      </value>
    </option>
```

- [ ] **Step 8: Fix `ReSharper.ReSharperLOCAL_VARIABLE_IDENTIFIER`**

Find and replace:
```xml
    <option name="ReSharper.ReSharperLOCAL_VARIABLE_IDENTIFIER">
      <value>
        <option name="FOREGROUND" value="C8D3F5" />
      </value>
    </option>
```
With:
```xml
    <option name="ReSharper.ReSharperLOCAL_VARIABLE_IDENTIFIER">
      <value>
        <option name="FOREGROUND" value="E26674" />
      </value>
    </option>
```

- [ ] **Step 9: Fix `ReSharper.ReSharperMUTABLE_LOCAL_VARIABLE_IDENTIFIER`**

Find and replace:
```xml
    <option name="ReSharper.ReSharperMUTABLE_LOCAL_VARIABLE_IDENTIFIER">
      <value>
        <option name="FOREGROUND" value="C8D3F5" />
      </value>
    </option>
```
With:
```xml
    <option name="ReSharper.ReSharperMUTABLE_LOCAL_VARIABLE_IDENTIFIER">
      <value>
        <option name="FOREGROUND" value="E26674" />
      </value>
    </option>
```

- [ ] **Step 10: Fix `ReSharper.ReSharperCAPTURED_VARIABLE_IDENTIFIER`**

Find and replace:
```xml
    <option name="ReSharper.ReSharperCAPTURED_VARIABLE_IDENTIFIER">
      <value>
        <option name="FOREGROUND" value="C8D3F5" />
      </value>
    </option>
```
With:
```xml
    <option name="ReSharper.ReSharperCAPTURED_VARIABLE_IDENTIFIER">
      <value>
        <option name="FOREGROUND" value="E26674" />
      </value>
    </option>
```

- [ ] **Step 11: Verify all Part 1 changes**

```bash
grep -E "E26674|65BCFF|E76572|56A3B1" "jetbrains-plugin/src/main/resources/colorSchemes/Electronic Moonlight.xml"
```

Expected: same count pattern as the `.icls` verification in Task 2 Step 11 — 5 lines with `E26674`, 1 with `65BCFF`, 2 with `E76572`, 2 with `56A3B1`.

---

### Task 6: Add Part 2 new attribute blocks to `colorSchemes/Electronic Moonlight.xml`

**Files:**
- Modify: `jetbrains-plugin/src/main/resources/colorSchemes/Electronic Moonlight.xml`

Same new attributes as Tasks 3 Step 1–2, but **without `#` prefix on all hex values**.

- [ ] **Step 1: Add `CSS_UNIT` to the CSS section**

Locate `CSS_VARIABLE` (the last entry in the CSS section). Insert immediately after it:

```xml
    <option name="CSS_UNIT">
      <value>
        <option name="FOREGROUND" value="D59DF6" />
      </value>
    </option>
```

- [ ] **Step 2: Add the JavaScript / TypeScript section**

Insert immediately after the `CSS_UNIT` block you just added:

```xml
    <!-- JavaScript / TypeScript -->
    <option name="JAVA_SCRIPT_LOCAL_VARIABLE">
      <value>
        <option name="FOREGROUND" value="E26674" />
      </value>
    </option>
    <option name="JAVA_SCRIPT_GLOBAL_VARIABLE">
      <value>
        <option name="FOREGROUND" value="FFC777" />
      </value>
    </option>
    <option name="JAVA_SCRIPT_PARAMETER">
      <value>
        <option name="FOREGROUND" value="FCA7EA" />
      </value>
    </option>
    <option name="JAVA_SCRIPT_INSTANCE_MEMBER_VARIABLE">
      <value>
        <option name="FOREGROUND" value="A9B8E8" />
      </value>
    </option>
    <option name="JAVA_SCRIPT_STATIC_MEMBER_VARIABLE">
      <value>
        <option name="FOREGROUND" value="FF966C" />
      </value>
    </option>
    <option name="JAVA_SCRIPT_FUNCTION_DECLARATION">
      <value>
        <option name="FOREGROUND" value="82AAFF" />
      </value>
    </option>
    <option name="JAVA_SCRIPT_INSTANCE_MEMBER_FUNCTION">
      <value>
        <option name="FOREGROUND" value="82AAFF" />
      </value>
    </option>
    <option name="JAVA_SCRIPT_STATIC_MEMBER_FUNCTION">
      <value>
        <option name="FOREGROUND" value="82AAFF" />
      </value>
    </option>
    <option name="JAVA_SCRIPT_KEYWORD">
      <value>
        <option name="FOREGROUND" value="C099FF" />
        <option name="FONT_TYPE" value="2" />
      </value>
    </option>
    <option name="JAVA_SCRIPT_REGEXP">
      <value>
        <option name="FOREGROUND" value="B4F9F8" />
      </value>
    </option>
    <option name="JAVA_SCRIPT_VALID_STRING_ESCAPE">
      <value>
        <option name="FOREGROUND" value="86E1FC" />
      </value>
    </option>
    <option name="JAVA_SCRIPT_TEMPLATE_LITERAL">
      <value>
        <option name="FOREGROUND" value="86E1FC" />
      </value>
    </option>
    <option name="JAVA_SCRIPT_MODULE_NAME">
      <value>
        <option name="FOREGROUND" value="C3E88D" />
      </value>
    </option>
```

- [ ] **Step 3: Verify new attributes present**

```bash
grep -c "JAVA_SCRIPT_" "jetbrains-plugin/src/main/resources/colorSchemes/Electronic Moonlight.xml"
```

Expected: `13`

```bash
grep "CSS_UNIT" "jetbrains-plugin/src/main/resources/colorSchemes/Electronic Moonlight.xml"
```

Expected: one line containing `CSS_UNIT`

- [ ] **Step 4: Validate XML is well-formed**

```bash
xmllint --noout "jetbrains-plugin/src/main/resources/colorSchemes/Electronic Moonlight.xml" && echo "XML valid"
```

Expected: `XML valid`

- [ ] **Step 5: Commit**

```bash
git add "jetbrains-plugin/src/main/resources/colorSchemes/Electronic Moonlight.xml"
git commit -m "feat: align plugin colorSchemes XML with VS Code syntax highlighting"
```

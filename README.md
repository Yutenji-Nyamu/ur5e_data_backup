# ur5e_data_backup

UR5e 真机**成功关节示范**，按采集日期 → 原始任务名 → 轨迹编号组织。

本次共 **64 条**已完成且人工标记成功的 schema v3 轨迹，含实测关节位置 `actual_q`、关节速度 `actual_qd` 和双相机图像。排除全部 23 条旧版仅 TCP 轨迹。盘点期间新增的 `20261005_162813` 已计入。

源数据 **11.835 GiB**，29,410 张 PNG（14,705 对双相机帧），约 25.37 分钟。图像、动作 CSV 和夹爪事件保留原始内容。

**Git 保存索引、session 和 CSV；图像随 [Release 分包](https://github.com/Yutenji-Nyamu/ur5e_data_backup/releases/tag/snapshot-2026-10-05) 下载。只运行 git clone 不包含图像。** 共 13 个 TAR 包，合计 11.856 GiB，每包小于 2 GB，不使用 Git LFS。

## 目录与下载

```text
2026-10-05/
└── plug_charger/
    └── 20261005_162813/
        ├── session.json
        ├── action.csv
        ├── gripper_events.csv
        ├── sync.csv
        └── images/{head,wrist}/frame_*.png
```

一级目录是采集日期（Asia/Shanghai），不是上传日期。

Python 3.12 或更新版本，无额外依赖：

```bash
git clone https://github.com/Yutenji-Nyamu/ur5e_data_backup.git
cd ur5e_data_backup
python3 restore.py --date 2026-10-05
# 全部日期：
python3 restore.py
```

也可直接下载 Release 附件，解压到仓库根目录。脚本只做常规下载、文件大小检查和解压，不要求逐文件哈希验证。保留 TAR 和解压数据时需约 24 GiB 空间。session 路径相对于其所在目录。

## 成功数据

| 原始任务名 | 轨迹数 | 源数据 GiB |
|---|---:|---:|
| `charger_plug` | 8 | 2.038 |
| `drawer_close` | 4 | 0.606 |
| `pick_place_cube` | 5 | 0.469 |
| `place_bread_basket` | 3 | 0.447 |
| `place_bread_skillet` | 3 | 0.427 |
| `place_empty_cup` | 3 | 0.500 |
| `plug_charger` | 16 | 2.716 |
| `pour_beans` | 5 | 1.195 |
| `sort_block` | 4 | 1.418 |
| `stack_blocks_three` | 5 | 0.963 |
| `stack_blocks_two` | 3 | 0.500 |
| `stack_blocks_two_0911` | 5 | 0.556 |

| 采集日期 | 轨迹数 |
|---|---:|
| [2026-09-08](2026-09-08/) | 16 |
| [2026-09-09](2026-09-09/) | 12 |
| [2026-09-10](2026-09-10/) | 3 |
| [2026-09-11](2026-09-11/) | 13 |
| [2026-09-12](2026-09-12/) | 5 |
| [2026-09-18](2026-09-18/) | 8 |
| [2026-10-05](2026-10-05/) | 7 |

## 说明

- 筛选的是含实测关节的原生 v3 轨迹；这类原始动作 CSV 同时保留同步 TCP 记录。旧版仅 TCP 的轨迹整体排除。
- 成功沿用采集时的人工标签，不代表自主策略成功率。任务命名保持原样，没有擅自合并别名或不同场景。
- 夹爪状态是开/关命令，独立事件 CSV 保留重复 close 等命令。
- 入选文件齐全，计数与索引相符。`20260918_171233` 有最大 0.4 秒采样间隔。
- 公开 session 副本去掉内网地址、设备序列号、串口路径和本机绝对根路径。图像和动作不做有损转换。抽查各轨迹首、中、尾双视角图像，没有发现明显人脸或私人屏幕；图像抽查不等于完整人工复核。
- 原采集目录未被移动、删除或修改；失败/中止/未复核数据、模型、环境和凭据不上传。固定快照截至 `20261005_162813`，后续采集不会自动上传。

托管规则参考：[GitHub 大文件说明](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github)。

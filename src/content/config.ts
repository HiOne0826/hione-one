import { defineCollection, z } from 'astro:content';

// 项目集合
const projects = defineCollection({
  schema: z.object({
    title: z.string(),
    description: z.string(),
    status: z.enum(['进行中', '已完成']),
    techStack: z.array(z.string()),
    image: z.string().optional(),
    demoUrl: z.string().optional(),
    repoUrl: z.string().optional(),
    publishDate: z.coerce.date(),
    updatedDate: z.coerce.date().optional(),
  }),
});

// 博客集合
const blog = defineCollection({
  schema: z.object({
    title: z.string(),
    description: z.string(),
    tags: z.array(z.string()),
    publishDate: z.coerce.date(),
    updatedDate: z.coerce.date().optional(),
  }),
});

// 碎碎念集合
const micro = defineCollection({
  schema: z.object({
    content: z.string(),
    tags: z.array(z.string()).optional(),
    publishDate: z.coerce.date(),
  }),
});

// 视频集合
const video = defineCollection({
  schema: z.object({
    title: z.string(),
    description: z.string(),
    platform: z.enum(['抖音', 'B站', 'YouTube']),
    url: z.string(),
    thumbnail: z.string().optional(),
    publishDate: z.coerce.date(),
  }),
});

export const collections = { projects, blog, micro, video };
